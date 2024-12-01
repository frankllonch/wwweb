from django.urls import path
from . import views

urlpatterns = [
    path("", views.services, name="services"),
    path("store/", views.store, name="store"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
]