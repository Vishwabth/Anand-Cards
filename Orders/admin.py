from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # No extra empty forms by default

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_price', 'status')  # Show key fields
    list_filter = ('status', 'order_date')  # Filter by status and order date
    search_fields = ('user__username', 'shipping_address')  # Search by username and address
    inlines = [OrderItemInline]  # Show the order items inline

    # You can add custom actions here
    actions = ['mark_as_dispatched', 'mark_as_delivered']

    def mark_as_dispatched(self, request, queryset):
        queryset.update(status='Dispatched')
    mark_as_dispatched.short_description = 'Mark selected orders as Dispatched'

    def mark_as_delivered(self, request, queryset):
        queryset.update(status='Delivered')
    mark_as_delivered.short_description = 'Mark selected orders as Delivered'

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
