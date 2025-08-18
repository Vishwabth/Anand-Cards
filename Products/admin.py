from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('name', 'category', 'price', 'stock', 'is_in_stock')

    # Fields to search in the admin search bar
    search_fields = ('name', 'category')  # Search by name and category

    # Method to display whether the product is in stock
    def is_in_stock(self, obj):
        return obj.stock == 'In stock'  # Returns a boolean indicating if the product is in stock
    is_in_stock.boolean = True  # This will display as a checkmark in the admin list

# Register Product model with ProductAdmin customization
admin.site.register(Product, ProductAdmin)
