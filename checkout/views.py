from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """set up our view for the checkout template"""
    bag = request.session.get('bag')
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KfrxTCFZ5MUgwOyPW7N4O2Hi881agVemSpuiBBg5chjcX3ghQSxGCq7CpXjoy0cr96cCylYXHyC800UpA94FKTG00kE2WsDgt',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
