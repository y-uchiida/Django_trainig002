from django.contrib import admin
from blog.models import Article
from blog.models import Comment
from blog.models import Tag

# 記事の管理画面から、タグとの関連を設定できるようにする
class TagInline(admin.TabularInline):
    model = Article.tags.through


class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = [
        "tags",
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
