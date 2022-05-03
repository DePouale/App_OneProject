from django.contrib import admin
from .models import Customer, Category, Product, ProductPhoto, Cart_product, Cart

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductPhoto)
admin.site.register(Cart_product)
admin.site.register(Cart)