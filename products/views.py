from rest_framework import viewsets
from .serializers import ProductSerializers
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers