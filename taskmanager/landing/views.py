from django.shortcuts import render


def index(request):
    return render(request, "landing/index.html")

def catalog(request):
    return render(request, "landing/catalog.html")