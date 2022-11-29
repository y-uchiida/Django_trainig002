from django.shortcuts import render, redirect
from blog.models import Article
from django.contrib.auth.views import LoginView
from .forms import UserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def index(request):
    popular_articles = Article.objects.order_by("-count")[:2]
    articles = Article.objects.all()[:3]
    context = {"title": "Really Site", "articles": articles, "popular_articles": popular_articles}
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
            user = form.save()
            login(request, user)
            messages.success(request, "ユーザー登録しました")
            return redirect("/")
    return render(request, "mysite/auth.html")


@login_required
def my_page(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "プロフィールを更新しました")

    return render(request, "mysite/my_page.html")
