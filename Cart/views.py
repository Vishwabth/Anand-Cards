from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Product
import json
from decimal import Decimal


@method_decorator(csrf_exempt, name='dispatch')
class ViewCartView(View):
    def get(self, request, *args, **kwargs):
        """Render the cart page with current cart items."""
        cart = request.session.get('cart', {})
        cart_items = []
        grand_total = Decimal(0)

        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(id=product_id)
                total_price = product.price * quantity
                grand_total += total_price
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'total_price': total_price,
                })
            except Product.DoesNotExist:
                continue  # Skip missing products

        return render(request, 'Cart/view_cart.html', {
            'cart_items': cart_items,
            'grand_total': grand_total
        })

    def post(self, request, *args, **kwargs):
        """Handle cart updates like add, increase, decrease, and remove."""
        try:
            data = json.loads(request.body)
            product_id = str(data.get('product_id'))
            action = data.get('action')

            if not product_id or not action:
                return JsonResponse({'error': 'Product ID and action are required.'}, status=400)

            cart = request.session.get('cart', {})

            if action == 'add' or action == 'increase':
                cart[product_id] = cart.get(product_id, 0) + 1
            elif action == 'decrease':
                if cart.get(product_id, 0) > 1:
                    cart[product_id] -= 1
                else:
                    cart.pop(product_id, None)
            elif action == 'remove':
                cart.pop(product_id, None)
            else:
                return JsonResponse({'error': 'Invalid action.'}, status=400)

            request.session['cart'] = cart
            request.session.modified = True

            # Calculate updated totals
            grand_total = Decimal(0)
            cart_items = []

            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                total_price = product.price * quantity
                grand_total += total_price
                cart_items.append({
                    'product_id': product_id,
                    'quantity': quantity,
                    'total_price': float(total_price),
                })

            return JsonResponse({
                'cart': cart_items,
                'grand_total': float(grand_total),
                'cart_count': sum(cart.values())
            })

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
