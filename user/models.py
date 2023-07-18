from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def _create_user(
        self,
        email,
        password,
        username=None,
        profile_img=None,
        is_staff=False,
        is_superuser=False,
        **extra_fields
    ):
        if not email:
            raise ValueError('User must have an email')

        now = timezone.localtime()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            profile_img=profile_img,
            is_staff=is_staff,
            is_superuser=is_superuser,
            date_joined=now,
            updated_at=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create_user
    def create_user(
        self, email, password, username=None, profile_img=None, **extra_fields
    ):
        # 회원가입 시에만 email의 '@' 전까지의 값으로 설정
        if not username:
            username = email.split('@')[0]
        return self._create_user(
            email, password, username, profile_img, False, False, **extra_fields
        )

    # create_superuser
    def create_superuser(
        self, email, password, username=None, profile_img=None, **extra_fields
    ):
        # 회원가입 시에만 email의 '@' 전까지의 값으로 설정
        if not username:
            username = email.split('@')[0]
        return self._create_user(
            email, password, username, profile_img, True, True, **extra_fields
        )


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=254)
    username = models.CharField(unique=True, max_length=254)
    profile_img = models.TextField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def set_username(self, username):
        self.username = username
        self.save()

    def set_profile_img(self, profile_img):
        self.profile_img = profile_img
        self.save()
