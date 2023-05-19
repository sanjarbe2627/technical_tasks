from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    """ Project User model"""

    username = models.CharField(
        max_length=255, unique=True, help_text=_("Username")
    )
    email = models.EmailField(
        max_length=255, unique=True, null=True, blank=True, help_text=_("User email")
    )
    fullname = models.CharField(
        max_length=100, null=True, blank=True, help_text=_("User Full name")
    )
    user_photo = models.ImageField(upload_to="users_photos/", null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, help_text=_("Date of registration"))
    is_active = models.BooleanField("is_active", default=True)
    is_staff = models.BooleanField("is_staff", default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.fullname}"

    def get_full_name(self):
        return f"{self.username}"

    def get_short_name(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['-date_joined']
