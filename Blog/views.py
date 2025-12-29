from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Blog

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