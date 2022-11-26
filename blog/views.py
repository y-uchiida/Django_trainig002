from django.shortcuts import render

from blog.models import Article


def article(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "blog/article.html", context)
