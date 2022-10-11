import random
from django.conf import settings
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL #auth.user

TAGS_MODEL_VALUES = ['electronics','cars','boats','movies']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self,query,user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2   = qs.filter(user=user).filter(lookup)
            qs = (qs|qs2).distinct()
        return qs

class ProductManager(models.Manager):

    def get_queryset(self,*args,**kwargs):
        return ProductQuerySet(self.model,using=self._db)

    def search(self,query,user=None):
        return Product.objects.is_public().filter(title__icontains=query)

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, default = 1, null=True, on_delete = models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(null = True, blank = True)
    price = models.DecimalField(max_digits = 15, decimal_places = 2, default = 99.99)
    public = models.BooleanField(default=True)
    object = ProductManager()

    def is_public(self) -> bool:
        return self.public

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self):
        return "123"

    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]