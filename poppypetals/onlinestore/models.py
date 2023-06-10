from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils.html import mark_safe
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.db import migrations

CATEGORY = (
    ('T','Tshirt'),
    ('SH','Shirt'),
    ('SK','Skirt'),
    ('P','Pant'),
    ('J','Jacket'),
    ('SO','Socks'),
    ('HB','Headband'),
    ('CO','Combination'),
    ('DU','Dungaree'),
    ('A','Accessories'),
)

LABEL = (
    ('N', 'New'),
    ('BS', 'Best Seller'),
)

TYPE_CHOICES = (
    ('B','Baby'),
    ('T','Toddler'),
    ('K','Kid'),
    ('AL','All'),
    ('TK','Toddler and Kid'),
    ('BK','Baby and Toddler'),
    
)

GENDER = (
    ('B','Boys'),
    ('G','Girls'),
    ('BT','Both'),
)

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY, max_length=2, null=True, blank=True)
    label = models.CharField(choices=LABEL,max_length=2, null=True, blank=True)
    type = models.CharField(choices=TYPE_CHOICES,max_length=8, null=True, blank=True)
    gender = models.CharField(choices=GENDER,max_length=8, null=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/product/")

    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("onlinestore:product", kwargs={"pk": self.pk})
    
    def get_add_to_cart_url(self) :
        return reverse("onlinestore:add-to-cart", kwargs={
            "pk" : self.pk
        })

    def get_remove_from_cart_url(self) :
        return reverse("onlinestore:remove-from-cart", kwargs={
            "pk" : self.pk
        })

    
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class ItemAdmin(admin.ModelAdmin):
    list_display=('item_name','price','category','label','type', 'gender', 'description', "image")
    
    def image(self, obj):
        return mark_safe(f'<img src="/media/{obj.image}" width="150" height="150" />')
    


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(default=1)
    item_id = models.CharField(max_length=100, unique=True)
