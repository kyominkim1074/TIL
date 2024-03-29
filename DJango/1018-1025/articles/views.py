from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

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
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            messages.success(request, "글 작성이 완료되었습니다.")
            return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/form.html", context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    context = {
        "article": article,
        'comments': article.comment_set.all(),
        'comment_form': comment_form
    }
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                messages.success(request, "글이 수정되었습니다.")
                return redirect("articles:detail", article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            "form": form,
        }
        return render(request, "articles/form.html", context)
    else:
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)
        

@login_required
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user:            
        if request.method == "POST":
            article.delete()
            messages.success(request, "글이 삭제되었습니다.")
            return redirect("articles:index")
        return render(request, "articles/detail.html")
    else:
        messages.warning(request, '작성자만 삭제할 수 있습니다.')
        return redirect('articles:detail', article.pk)

@login_required
def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)

@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        if request.method=='POST':
            comment.delete()
            return redirect('articles:detail', article_pk)
    else:
        messages.warning(request, '작성자만 삭제할 수 있습니다..')
        return redirect('articles:detail', article_pk)
    
@login_required
def likes(request, article_pk):
    article=get_object_or_404(Article, pk=article_pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:detail', article_pk)

@login_required
def dislikes(request, article_pk):
    article=get_object_or_404(Article, pk=article_pk)
    if request.user in article.dislike_users.all():
        article.dislike_users.remove(request.user)
    else:
        article.dislike_users.add(request.user)
    return redirect('articles:detail', article_pk)