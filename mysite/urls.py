from django.urls import path
from mysite import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup", views.signup, name="signup"),
    path("my-page", views.my_page, name="my_page"),
]
