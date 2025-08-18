from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Order, OrderItem
from Products.models import Product
from decimal import Decimal
import json
from django.http import HttpResponse
from django.views import View
from django.template.loader import render_to_string



class CheckoutView(View):

    def calculate_grand_total(self, cart):
        """Helper method to calculate the total price of cart items."""
        total = Decimal(0)
        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(id=product_id)
                total += product.price * quantity
            except Product.DoesNotExist:
                continue
        return total

    def get(self, request, *args, **kwargs):
        """Render the checkout page with cart items and total."""
        cart = request.session.get('cart', {})
        cart_items = []
        grand_total = self.calculate_grand_total(cart)

        # Get product details for each item in the cart
        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(id=product_id)
                total_price = product.price * quantity
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'total_price': total_price
                })
            except Product.DoesNotExist:
                continue  # Skip missing products

        return render(request, 'Orders/checkout.html', {
            'cart_items': cart_items,
            'grand_total': grand_total
        })

    def post(self, request, *args, **kwargs):
        """Handle the order placement from the cart data."""
        cart = request.session.get('cart', {})
        if not cart:
            return redirect('view_cart')  # If cart is empty, redirect to view cart page

        # Get product details for the cart items
        cart_items = []
        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(id=product_id)
                total_price = product.price * quantity
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'total_price': total_price
                })
            except Product.DoesNotExist:
                continue  # Skip missing products

        # Validate form data
        shipping_address = request.POST.get('shipping_address')
        if not shipping_address:
            return render(request, 'Orders/checkout.html', {
                'error_message': 'Shipping address is required.',
                'cart_items': cart_items,
                'grand_total': self.calculate_grand_total(cart)
            })

        # Hardcoded payment method
        payment_method = 'COD'

        # Create the order
        order = Order.objects.create(
            total_price=self.calculate_grand_total(cart),
            shipping_address=shipping_address,
            payment_method=payment_method,
            status='pending'
        )

        # Create OrderItems and clear the session cart
        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price
                )
            except Product.DoesNotExist:
                continue  # Skip missing products

        # Clear cart after order is placed
        request.session['cart'] = {}
        request.session.modified = True

        # Redirect to the order confirmation page with the created order's pk
        return redirect('order_confirmation', pk=order.pk)


class OrderConfirmationView(View):
    def get(self, request, pk, *args, **kwargs):
        """Display the order confirmation page."""
        order = get_object_or_404(Order, pk=pk, status='pending')
        return render(request, 'Orders/order_confirmation.html', {'order': order})

    def post(self, request, pk, *args, **kwargs):
        """When the admin confirms the order."""
        order = get_object_or_404(Order, pk=pk, status='pending')
        order.status = 'confirmed'
        order.save()
        return redirect('order_confirmation_success')


