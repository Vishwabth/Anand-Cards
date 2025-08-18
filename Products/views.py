from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

def product_list_view(request):
    category = request.GET.get('category', 'Hindu Cards')

    if category == 'Muslim Cards':
        template_name = 'Products/muslimcards.html'
    elif category == 'Worship Cards':
        template_name = 'Products/worshipcards.html'
    else:
        template_name = 'Products/hinducards.html'

    print(f"Using template: {template_name}")  # Debugging output

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, template_name, {'products': page_obj})
def get_queryset(self):
    category = self.request.GET.get('category', 'Hindu Cards')
    if category:
        products = Product.objects.filter(category=category)
        print(f"Fetched {products.count()} products for category: {category}")  # Debugging output
        return products
    return Product.objects.all()


