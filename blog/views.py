from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from datetime import datetime

def blog(request):
    posts = Post.objects.filter(published_date__lt = datetime.now(), status= 1) 
    context = {"posts" : posts}
    return render(request, 'blog/blog-home.html', context)


def single_blog(request, pid):
    #__gt : greater than      __lt : less than
    posts = list(Post.objects.filter(published_date__lt = datetime.now(), status= 1))
    post = get_object_or_404(Post,status=1, pk = pid)
    if post.login_require == True and not request.user.is_authenticated:
        return redirect("accounts:login")
    
    index = posts.index(post)
    next_post = 0
    if index == len(posts) - 1:
        next_post = posts[0]
    else:
        next_post = posts[index+1]
    context = {"post" : post, "prev" : posts[index - 1], "next" : next_post}
    return render(request, 'blog/blog-single.html', context)




def test(request, pid):
    # post = get_object_or_404(Post, pk=pid)
    posts = Post.objects.filter(published_date__lt = datetime.now()) #__gt : greater than      __lt : less than
    post = get_object_or_404(Post,status=1, pk = pid)
    context = {"posts" : post}
    return render(request,'test.html', context)

    


def resume_view(request):
    return render(request, "cv/index.html")
    