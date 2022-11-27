from django.urls import path
from mysite import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.Login.as_view()),
    path("logout/", LogoutView.as_view()),
]
