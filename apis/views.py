from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serilizers import ProductSeralizer


# Create your views here.

class Productvieset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer