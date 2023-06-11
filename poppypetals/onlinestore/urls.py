from django.urls import path, include
from . import views

app_name = 'onlinestore'

urlpatterns = [
    path('', views.home, name='home',),
    path('baby_page/', views.baby, name='baby'),
    path('toddler_page/', views.toddler, name='toddler',),
    path('kid_page/', views.kid, name='kid',),
    path('accessories_page/', views.accessories, name='accessories',),
    path('aboutus/', views.aboutus, name='aboutus',),
    path('cart/', views.cart, name='cart',),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),


   
]
