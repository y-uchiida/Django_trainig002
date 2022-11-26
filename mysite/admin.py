from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from mysite.models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = ((None, {"fields": ("email", "password")}), (None, {"fields": ("is_active", "is_admin")}))
    list_display = ("email", "is_active")
    list_filter = ()
    ordering = ()
    filter_horizontal = ()


# 作成したUserモデルを、CustomUserAdminの表示形式で管理サイトに登録する
admin.site.register(User, CustomUserAdmin)
