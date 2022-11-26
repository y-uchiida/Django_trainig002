from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Article


def index(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    page_number = request.GET.get("page")
    context = {"articles": paginator.get_page(page_number), "page_number": page_number}
    return render(request, "blog/blogs.html", context)


def article(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "blog/article.html", context)
