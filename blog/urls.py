from django.urls import path
from blog import views

urlpatterns = [path("", views.index, name="index"), path("article/<int:pk>", views.article, name="article")]
