from django.db import models
from django.core.validators import RegexValidator

class Customer(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField(
        unique = True
        )
    phoneNumberRegex = RegexValidator(
        regex = r"^\+?1?\d{8,15}$"
        )

    phoneNumber = models.CharField(
        validators = [phoneNumberRegex], 
        max_length = 16, 
        unique = True
        )
        
    class Meta:
        verbose_name = ("Клиент")
        verbose_name_plural = ('Клиенты')

    def __str__(self):
        return f' Имя: {self.first_name} | Фамилия: {self.last_name}'

class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()


    class Meta:
        verbose_name = ("Категория")
        verbose_name_plural = ('Категории')

    def __str__(self):
        return f'{self.name} '

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(name="Нет Категории")
        return obj.pk

class Product(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    created_up = models.DateTimeField(auto_now_add=False, auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        default=Category.get_default_pk
    )

    class Meta:
        verbose_name = ("Товар")
        verbose_name_plural = ('Товары')

    def __str__(self):
        return f'{self.name} {self.price} рублей'

class ProductPhoto(models.Model):

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static\media\product_photo')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = ("Фотография")
        verbose_name_plural = ('Фотографии')

    def __str__(self):
        return f'{self.id}   {self.product_id}'