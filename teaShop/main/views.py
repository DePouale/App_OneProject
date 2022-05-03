from django.shortcuts import render
from services.models import Category, Product

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def category(request):
    category = Category.objects.all
    return render(request, "main/category.html", {'title': 'Каталог чая', 'category': category})

def articles(request):
    return render(request, "main/articles.html", {'title': 'Статьи', 'articles': articles})

def ulun(request):
    product = Product.objects.order_by('id')  
    return render(request, "main/ulun.html", {'title': 'Улун', 'product': product})
