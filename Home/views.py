from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from Products.models import Product  # Assuming you have a Product model

def home(request):
    return render(request, 'Home/home.html')
from django.views import View
from django.shortcuts import render
from difflib import get_close_matches

from django.views import View
from django.shortcuts import render
from difflib import get_close_matches

class SearchView(View):
    def get(self, request, *args, **kwargs):
        # Get the search query from the GET request
        query = request.GET.get('q', '').lower().strip()

        # Define the mapping of categories to templates
        options = {
            "muslim": "Products/muslimcards.html",
            "muslim cards": "Products/muslimcards.html",
            "worship cards": "Products/worshipcards.html",
            "hindu": "Products/worshipcards.html",
            "hindu cards": "Products/hinducards.html",
            "puja": "Products/hinducards.html",
            "puja cards": "Products/hinducards.html",
        }

        # Find the closest match to the query
        best_match = get_close_matches(query, options.keys(), n=1, cutoff=0.3)

        if best_match:
            template_name = options[best_match[0]]
            print(f"Using template: {template_name}")  # Debugging output
            return render(request, template_name)
        else:
            print("No matching cards found.")  # Debugging output
            return render(request, 'Home/home.html', {'message': 'No matching cards found.'})


