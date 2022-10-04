from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by("-pk")
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def create(request):
    # db에 저장하는 로직을 만든다.
    # 조건문을 통해 아무 내용도 없이 db에 저장되는 일을 방지해준다.
    # POST 메서드는 GET과 다르게 데이터를 URL이 아니라 페이지 내부로 데이터를 전송한다.
    # CRUD의 Create에 해당한다.
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/new.html", context=context)


def detail(request, pk):
    # 특정 pk에 해당하는 글을 가져온다.(get)
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # POST 요청이면 폼 데이터를 처리한다
    if request.method == "POST":
        # 폼 인스턴스를 생성하고 요청에 의한 데이타로 채운다
        article_form = ArticleForm(request.POST, instance=article)
        # 폼이 유효한지 체크한다
        if article_form.is_valid():
            # 유효했을 경우 데이터를 저장하고 디테일 페이지로 이동한다.
            article_form.save()
            return redirect("articles:detail", article.pk)
        # 유효하지 않다면 render함수를 호출된다.
        # 이 때 context로 넘겨지는 값에 오류 메세지를 포함된다.
    else:
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
    }
    return render(request, "articles/update.html", context)


def delete(request, pk):
    review = Article.objects.get(pk=pk)
    review.delete()
    return redirect("articles:index")
