from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='imges/')
    
    CATEGORY_CHOICES = [
        ('Hindu Cards', 'Hindu Cards'),
        ('Muslim Cards', 'Muslim Cards'),
        ('Worship Cards', 'Worship Cards'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    STOCK_CHOICES = [
        ('In stock', 'In stock'),
        ('Out of stock', 'Out of stock'),
    ]
    stock = models.CharField(max_length=20, choices=STOCK_CHOICES, default='In stock')

    def __str__(self):
        return f"{self.name} ({self.category})"
