from django.shortcuts import render, get_object_or_404
from .models import Post

def showblog(request):
    posts = Post.objects.all()
    length = len(list(Post.objects.all()))
    return render(request, 'blog/blog.html', {'posts': posts, 'length': length})

def post_detailes(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    length = len(list(Post.objects.all()))
    if post_id > 1:
        prev = post_id - 1
    else:
        prev = post_id
    if post_id < length:
        next = post_id + 1
    else:
        next = post_id
        
    
    return render(request, 'blog/post_detailes.html', {'post': post, 'prev': prev, 'next': next, 'length': length})