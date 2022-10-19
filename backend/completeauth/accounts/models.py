from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager




class User(AbstractUser):
    username = None
    email = models.EmailField( unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=4 , null=True, blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return self.email
class Department(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length = 250)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length = 250)
    visitors = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name