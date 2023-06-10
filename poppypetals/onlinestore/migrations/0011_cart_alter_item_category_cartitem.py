# Generated by Django 4.2 on 2023-06-09 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('onlinestore', '0010_item_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, choices=[('T', 'Tshirt'), ('SH', 'Shirt'), ('SK', 'Skirt'), ('P', 'Pant'), ('J', 'Jacket'), ('SO', 'Socks'), ('HB', 'Headband'), ('CO', 'Combination'), ('DU', 'Dungaree'), ('A', 'Accessories')], max_length=2, null=True),
        ),
        
    ]