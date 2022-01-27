from django.shortcuts import render

def showblog(request):
    return render(request, 'blog/blog.html')
