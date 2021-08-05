from django.shortcuts import render
from wall_blogs.models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home_page.html', context)