from django.contrib import admin
from blog.models import Article
from blog.models import Comment


admin.site.register(Article)
admin.site.register(Comment)
