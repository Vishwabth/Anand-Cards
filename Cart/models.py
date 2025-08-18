from django.db import models
from django.conf import settings
from Products.models import Product

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='cart_items'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        user_display = self.user.username if self.user else "Guest"
        return f"{user_display} - {self.product.name} ({self.quantity})"

    def total_price(self):
        return (self.product.price or 0) * self.quantity

    def save(self, *args, **kwargs):
        if self.quantity < 1:
            self.quantity = 1
        super().save(*args, **kwargs)
