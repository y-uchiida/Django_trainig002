from django.shortcuts import render
from blog.models import Article
from django.contrib.auth.views import LoginView


def index(request):
    articles = Article.objects.all()[:3]
    context = {"title": "Really Site", "articles": articles}
    return render(request, "mysite/index.html", context)


class Login(LoginView):
    template_name = "mysite/login.html"
