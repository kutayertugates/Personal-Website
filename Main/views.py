from django.shortcuts import render
from Blog.models import Blog

def homepage(request):
    latest_posts = Blog.objects.select_related('author')\
                               .prefetch_related('tags')\
                               .order_by('-created_at')[:5]

    context = {
        'latest_posts': latest_posts
    }
    
    return render(request, 'Main/index.html', context)