from turtle import title
from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    # 1. db에서 모든글을 불러온다.
    posts = Post.objects.all()
    # 2. template에 보내준다.
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def new(request):
    return render(request, "posts/new.html")


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    Post.objects.create(title=title, content=content)

    context = {
        "title": title,
        "content": content,
    }
    return redirect("posts:index")


def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()
    return redirect("posts:index")


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "posts/detail.html", context)


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post,
    }
    return render(request, "posts/edit.html", context)


def update(request, pk):
    post = Post.objects.get(pk=pk)
    title_ = request.GET.get("title")
    content_ = request.GET.get("content")

    post.title = title_
    post.content = content_
    post.save()
    return redirect("posts:detail", post.pk)
