from django.urls import path
from .views import ProductViewSet,ProductModelViewSet

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('', ProductModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-model-list'),
]