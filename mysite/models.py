from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager["User"]):
    # BaseUSerManager が参照するModel type を "User"として渡しておかないと、以下のエラーが出る
    # Django のManager クラスがGeneric として宣言されていることが原因らしい
    # Missing type parameters for generic type "BaseUserManager"
    # https://github.com/typeddjango/django-stubs#why-am-i-getting-incompatible-return-type-errors-on-my-custom-managers
    def create_user(self, email, password: str | None = None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        app_label = "mysite"

    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField("mysite.User", unique=True, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(default="匿名ユーザー", max_length=30)
    zipcode = models.CharField(default="", max_length=8)
    prefecture = models.CharField(default="", max_length=6)
    city = models.CharField(default="", max_length=100)
    address = models.CharField(default="", max_length=200)

    class Meta:
        app_label = "mysite"


# def create_recode(user) -> Profile:
#     profile = Profile.objects.create(user=user)
#     return profile

# Userのレコードが作成されたとき、同時にProfile のレコードも作成する
# @receiver デコレータで、User レコードが作成されたときに起動するように指定
@receiver(post_save, sender="mysite.User")
def create_one_to_one(sender, **kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=kwargs["instance"])
