from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticlForm

from .forms import ArticleForm
from .models import Article

# Create your views here.

# Create your views here.
def index(request):
    article = Article.objects.order_by("-pk")
    context = {
        "article": article,
    }
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(reques, "글 작성이 완료되었습니다.")
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/create.html", context=context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        "movie": movie,
    }
    return render(request, "movies/detail.html", context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("movies:detail", movie.pk)
    else:
        movie_form = MovieForm(instance=movie)
    context = {
        "movie_form": movie_form,
    }
    return render(request, "movies/update.html", context=context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie.delete()
        return redirect("movies:index")
    return render(request, "movies/detail.html")
