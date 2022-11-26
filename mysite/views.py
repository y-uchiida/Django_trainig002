from django.shortcuts import render
from blog.models import Article


def index(request):
    articles = Article.objects.all()[:3]
    context = {"title": "Really Site", "articles": articles}
    return render(request, "mysite/index.html", context)
