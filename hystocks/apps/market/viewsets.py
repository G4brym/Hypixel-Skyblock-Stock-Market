from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from hystocks.apps.market.models import ProductMarketPrice
from hystocks.apps.products.models import Product
from hystocks.apps.products.serializers import ProductSerializer


class ProductMarketPriceViewSet(GenericViewSet):
    queryset = ProductMarketPrice.objects.all()

    @action(detail=True, methods=['get'])
    def prices(self, request, pk):
        return Response({
            "product": ProductSerializer(Product.objects.get(pk=pk)).data,
            "data": ProductMarketPrice.objects.filter(product_id=pk).values_list(
                "open_time", "open", "high", "low", "close"
            ).order_by("open_time")
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def movers(self, request, pk):
        return Response({
            "product": ProductSerializer(Product.objects.get(pk=pk)).data,
            "data": ProductMarketPrice.objects.filter(product_id=pk).values_list(
                "open_time", "open", "high", "low", "close"
            ).order_by("open_time")
        }, status=status.HTTP_200_OK)
