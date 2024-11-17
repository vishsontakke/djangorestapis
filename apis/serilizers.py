from rest_framework import serializers
from .models import Product

class ProductSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'discription', 'price', 'stock', 'created_at', 'updated_at']
