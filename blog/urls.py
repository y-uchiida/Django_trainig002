from django.urls import path
from blog import views

urlpatterns = [path("article/<int:pk>", views.article, name="article")]
