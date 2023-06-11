from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from django.views.decorators.http import require_POST


def home(request):    
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        username = request.user.username
        context = {'user_id': user_id, 'username': username, 'items': Item.objects.all()}
        return render(request, 'onlinestore/home.html', context)

        
    else:
        context = {
            'items': Item.objects.all()
        }
        return render(request, 'onlinestore/home.html', context)




# @login_required
# def user_dashboard(request):
#     current_user = request.user
#     user_id = current_user.id
#     username = request.user.username
#     context = {'user_id': user_id, 'username': username}
#     return render(request, 'onlinestore/home.html',context)

@login_required
def add_to_cart(request, item_id):
    # Get the user's cart or create a new one if it doesn't exist
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Create a new cart item and associate it with the user's cart
    item = CartItem(cart=cart, item_id=item_id)
    quantity = CartItem.quantity if CartItem else 0
    item.save()

    return redirect('onlinestore.cart')

@login_required
@require_POST
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('onlinestore.cart')

@login_required
@require_POST
def update_quantity(request, item_id):
    quantity = int(request.POST['quantity'])
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.quantity = quantity
    item.save()
    return redirect('onlinestore.cart')


def baby(request):
    baby_items = Item.objects.filter(type='B' and 'BK')
    context = {
        'baby_items': baby_items
    }
    return render(request, 'onlinestore/baby.html', context)

def toddler(request):
    toddler_items = Item.objects.filter(type='T' and 'TK')
    context = {
        'toddler_items': toddler_items
    }
    return render(request, 'onlinestore/toddler.html', context)

def kid(request):
    kid_items = Item.objects.filter(type='K' and 'TK')
    context = {
        'kid_items': kid_items
    }
    return render(request, 'onlinestore/kid.html', context)

def accessories(request):
    accessories_items = Item.objects.filter(type='A')
    context = {
        'accessories_items': accessories_items
    }
    return render(request, 'onlinestore/accessories.html', context)

def aboutus(request):
    context = {}
    
    return render(request, 'onlinestore/aboutus.html', context)

def store(request):
    context = {}
    return render(request, 'onlinestore/store.html', context)

def cart(request):
    context = {}
    return render(request, 'onlinestore/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'onlinestore/checkout.html', context)