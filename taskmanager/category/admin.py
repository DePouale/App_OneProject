from django.contrib import admin
from .models import Category, Customer, OrderItems, Product, Order
# Register your models here.

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItems)
