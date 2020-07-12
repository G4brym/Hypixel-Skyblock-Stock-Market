from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from hystocks.apps.products.models import Product
from hystocks.apps.products.serializers import ProductSerializer


class ProductViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = None
