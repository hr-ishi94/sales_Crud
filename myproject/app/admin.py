from django.contrib import admin
from .models import Sales

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    
    list_display=['product_ID', 'category', 'date', 'price', 'discount', 'units_sold']