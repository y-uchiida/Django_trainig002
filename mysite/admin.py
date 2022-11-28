from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from mysite.models import User
from mysite.models import Profile

# adminでuser作成用に追加
from mysite.forms import UserCreationForm


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete: bool = False


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                ),
            },
        ),
        (
            None,
            {
                "fields": (
                    "is_active",
                    "is_admin",
                ),
            },
        ),
    )
    list_display = ("email", "is_active")
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                ),
            },
        ),
    )
    add_form = UserCreationForm


# adminでuser作成用に追加
add_form = UserCreationForm

# 作成したUserモデルを、CustomUserAdminの表示形式で管理サイトに登録する
admin.site.register(User, CustomUserAdmin)

admin.site.register(Profile)
