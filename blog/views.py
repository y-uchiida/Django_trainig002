from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Article, Comment
from blog.forms import CommentForm


def index(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    page_number = request.GET.get("page")
    context = {"articles": paginator.get_page(page_number), "page_number": page_number}
    return render(request, "blog/blogs.html", context)


def article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        if request.POST.get("like_count", None):
            article.count += 1
            article.save()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()

    comments = Comment.objects.filter(article=article)
    context = {"article": article, "comments": comments}

    return render(request, "blog/article.html", context)
