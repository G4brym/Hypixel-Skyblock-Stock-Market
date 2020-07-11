from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from hystocks.apps.market.models import ProductMarketPrice


class ProductMarketPriceViewSet(GenericViewSet):
    queryset = ProductMarketPrice.objects.all()

    @action(detail=True, methods=['get'])
    def prices(self, request, pk):
        return Response(ProductMarketPrice.objects.filter(product_id=pk).values_list(
            "open_time", "open", "high", "low", "close"
        ), status=status.HTTP_200_OK)
