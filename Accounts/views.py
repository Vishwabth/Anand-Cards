from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Orders.models import Order
from Wishlists.models import Wishlist
from Cart.models import Cart

class AccountPageView(LoginRequiredMixin, TemplateView):
    template_name = 'Accounts/account_page.html'  # Path to your template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['orders'] = Order.objects.filter(user=user)  # Fetch user orders
        context['wishlist_items'] = Wishlist.objects.filter(user=user)              # Fetch user wishlist
        context['cart_items'] = Cart.objects.filter(user=user)                      # Fetch user cart
        return context
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        # Add custom logic here if needed
        return super().form_valid(form)
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django import forms

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class SignupView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('account_page')

    def form_valid(self, form):
        # Save the user and log them in
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')  # Replace 'home' with your desired redirect URL name

