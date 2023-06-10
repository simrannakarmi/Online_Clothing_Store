from django.contrib import admin
from .models import Item, OrderItem, Order
from django.utils.html import mark_safe
from django.utils.html import format_html

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)


# Register your models here.
# @admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=('item_name','price','category','label','type', 'gender', 'description', "image")
    
    def image(self, obj):
        return mark_safe(f'<img src="/media/{obj.image}" width="150" height="150" />')