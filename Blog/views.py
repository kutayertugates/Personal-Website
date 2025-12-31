from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.db.models import Q
from .models import Blog, Tag

def Index(request):
    posts = Blog.objects.select_related('author').prefetch_related('tags').order_by('-created_at')

    # --- FİLTRELEME MANTIĞI ---

    # 2. Etiket Filtreleme (?tag=backend&tag=frontend)
    # getlist kullanıyoruz çünkü birden fazla 'tag' parametresi gelebilir.
    selected_tags = request.GET.getlist('tag') 
    
    if selected_tags:
        # 'slug__in' -> Seçilen slug'lardan HERHANGİ BİRİNE sahipse getir (OR mantığı)
        posts = posts.filter(tags__slug__in=selected_tags)

    # 3. Arama Filtreleme (?q=arama+terimi)
    search_query = request.GET.get('q')
    
    if search_query:
        # Başlıkta, içerikte, meta açıklamada VEYA etiket adında arama yap
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(meta_description__icontains=search_query) |
            Q(tags__name__icontains=search_query)
        )

    # 4. Duplicate (Tekrar) Önleme
    # ManyToMany ilişkilerde filtreleme yapınca bazen aynı yazı 2 kere gelebilir.
    # distinct() bunu engeller.
    posts = posts.distinct()

    # --- UI İÇİN CONTEXT ---
    
    # Tüm etiketleri çekelim ki sidebar'da listeleyelim
    all_tags = Tag.objects.all()

    context = {
        'posts': posts,
        'all_tags': all_tags,
        # Filtreleri template'e geri gönderiyoruz ki inputlar dolu kalsın (UX Kuralı)
        'selected_tags': selected_tags, 
        'search_query': search_query,
    }
    
    return render(request, 'Blog/index.html', context=context)

def Detail(request, slug):
    # 1. Yazıyı Getir (Performanslı Sorgu)
    # select_related('author') -> Yazarı JOIN ile getirir (Ekstra sorgu atmaz)
    # prefetch_related('tags') -> Etiketleri verimli şekilde getirir
    post = get_object_or_404(
        Blog.objects.select_related('author').prefetch_related('tags'), 
        slug=slug
    )
    
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Blog.objects.filter(tags__in=post_tags_ids)\
                                .exclude(id=post.id)\
                                .annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags', '-created_at')\
                                .distinct()[:3] # Sadece 3 tane göster

    context = {
        'post': post,
        'similar_posts': similar_posts
    }
    
    return render(request, 'Blog/detail.html', context)