from django.shortcuts import render
from blog.models import Article
from django.contrib.auth.views import LoginView
from .forms import UserCreationForm


def index(request):
    articles = Article.objects.all()[:3]
    context = {"title": "Really Site", "articles": articles}
    return render(request, "mysite/index.html", context)


class Login(LoginView):
    template_name = "mysite/auth.html"


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
    return render(request, "mysite/auth.html")
