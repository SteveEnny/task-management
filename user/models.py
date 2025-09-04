# Create your models here.

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)


class UserManger(BaseUserManager):
    """Manger for users"""

    def create_user(self, email, password, **extra_fields):
        """Create save and return a new user"""
        if not email:
            raise ValueError("User must have an email")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    objects = UserManger()

    USERNAME_FIELD = 'email'
