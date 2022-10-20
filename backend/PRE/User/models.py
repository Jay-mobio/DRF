from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    TYPE = (
        ('social','social'),
        ('custom','custom'),
    )

    username = None
    email = models.EmailField(unique = True, blank = True)
    mobile = models.IntegerField()
    address = models.TextField()
    profile_pic = models.ImageField(null = True, blank = True, default = "profiel.jpg")
    signup_type = models.CharField(max_length = 200, null = True, choices = TYPE, blank = True, default = 'social')
    created_at = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now_add = True, null = True)
    created_by = models.CharField(max_length = 250, null = True, blank = True)
    updated_by = models.CharField(max_length = 250, null = True, blank = True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
