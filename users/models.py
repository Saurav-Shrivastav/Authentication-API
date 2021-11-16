import sys
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from users.managers import UserManager


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False, null=True)
    is_admin = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True, null=True)
    is_superuser = models.BooleanField(default=False, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
    ]

    objects = UserManager()

    def __str__(self):
        return f"{self.name}"

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
