"""
URL configuration for Ac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from Orders.views import CheckoutView, OrderConfirmationView
from django.urls import path, include
from Home.views import home,SearchView
from django.urls import reverse

from django.contrib import admin
from django.urls import path
from Products.views import product_list_view
from Cart.views import ViewCartView
from Orders.views import CheckoutView, OrderConfirmationView
from Wishlists.views import ViewWishlistView
from django.conf import settings
from django.conf.urls.static import static
from Accounts.views import AccountPageView,CustomLoginView,SignupView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # Products routes
    path('Products/', product_list_view, name='product_list'),  # Renders products/product_list.html

    # Cart routes
    #path('cart/add/<int:pk>/', AddToCartView.as_view(), name='add_to_cart'),  # Renders cart/add_to_cart.html
    path('cart/', ViewCartView.as_view(), name='view_cart'),  # Renders cart/view_cart.html
    #path('cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove_from_cart'),  # Renders cart/remove_from_cart.html

    # Orders routes
    path('checkout/', CheckoutView.as_view(), name='checkout'),  # Renders orders/checkout.html
    path('order_confirmation/<int:pk>/', OrderConfirmationView.as_view(), name='order_confirmation'),# Renders orders/order_confirmation.html
    # Wishlist routes
   path('wishlists/', ViewWishlistView.as_view(), name='view_wishlist'),
   path('search/', SearchView.as_view(), name='search'),
   path('accounts/', AccountPageView.as_view(), name='account_page'),
   path('login/', CustomLoginView.as_view(), name='login'),
   path('signup/', SignupView.as_view(), name='signup'),
   path('logout/', LogoutView.as_view(), name='logout'),

   #path('order/<int:order_id>/pdf/', GeneratePDFView.as_view(), name='generate_pdf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

