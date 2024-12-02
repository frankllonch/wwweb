from django.shortcuts import render, get_object_or_404
from services.models import Service  # Import the Service model from core


def product_detail(request, pk):
    product = get_object_or_404(Service, pk=pk)
    return render(request, "services/product_detail.html", {"product": product})

def services(request):
    products = Service.objects.all()
    return render(request, "services/services.html", {"products": products})

