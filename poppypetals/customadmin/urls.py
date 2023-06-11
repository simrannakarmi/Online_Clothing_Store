from django.contrib import admin 
from django.urls import path  

# admin.site.site_header = 'Poppy Petals Admin'

urlpatterns = [
     path('admin/', admin.site.urls),
 ]