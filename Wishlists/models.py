from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from Products.models import Product

class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist_items')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
