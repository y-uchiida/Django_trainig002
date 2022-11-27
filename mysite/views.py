from django.shortcuts import render, redirect
from blog.models import Article
from django.contrib.auth.views import LoginView
from .forms import UserCreationForm
from django.contrib import messages


def index(request):
    articles = Article.objects.all()[:3]
    context = {"title": "Really Site", "articles": articles}
    return render(request, "mysite/index.html", context)


class Login(LoginView):
    template_name = "mysite/auth.html"

    def form_valid(self, form):
        messages.success(self.request, "ログインしました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "メールアドレスまたはパスワードが正しくありません")
        return super().form_invalid(form)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "ユーザー登録しました")
            return redirect("/")
    return render(request, "mysite/auth.html")
