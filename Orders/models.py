from django.db import models
from django.conf import settings
from Products.models import Product  # Import Product model
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('COD', 'Cash on Delivery'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Default to 0
    shipping_address = models.TextField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, default='COD')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order {self.id} - {self.user.username if self.user else 'Guest'} ({self.status})"

    def calculate_total_price(self):
        # Sum the total price of all related order items
        return sum(item.total_price() for item in self.order_items.all())

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order.id} - {self.product.name} x {self.quantity}"

    def total_price(self):
        return self.quantity * self.price
