from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Product
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class ViewWishlistView(View):
    def get(self, request, *args, **kwargs):
        # Retrieve the wishlist from the session
        wishlist = request.session.get('wishlist', {})
        wishlist_items = []

        # Fetch product details from the database
        for product_id in wishlist.keys():
            try:
                product = Product.objects.get(id=product_id)
                wishlist_items.append({'product': product})
            except Product.DoesNotExist:
                continue  # Skip any invalid product IDs

        return render(request, 'Wishlists/view_wishlist.html', {
            'wishlist_items': wishlist_items,
        })

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            product_id = str(data.get('product_id'))  # Ensure product_id is a string for dictionary keys
            action = data.get('action')  # Action: 'add', 'remove'

            if not product_id or not action:
                return JsonResponse({'message': 'Product ID or action is missing!'}, status=400)

            # Retrieve the wishlist from the session
            wishlist = request.session.get('wishlist', {})

            if action == 'add':
                # Add the product to the wishlist if not already present
                if product_id not in wishlist:
                    wishlist[product_id] = 1  # Use `1` to signify presence
            elif action == 'remove':
                # Remove the product from the wishlist
                if product_id in wishlist:
                    del wishlist[product_id]
            else:
                return JsonResponse({'message': 'Invalid action!'}, status=400)

            # Save the updated wishlist back to the session
            request.session['wishlist'] = wishlist

            # Count the total number of items in the wishlist
            wishlist_count = len(wishlist)

            return JsonResponse({
                'message': 'Wishlist updated successfully!',
                'wishlist_count': wishlist_count,
            }, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data!'}, status=400)
        except Exception as e:
            return JsonResponse({'message': f'An error occurred: {str(e)}'}, status=500)
