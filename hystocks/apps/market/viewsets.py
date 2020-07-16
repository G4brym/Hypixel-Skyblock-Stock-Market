from datetime import timedelta
from decimal import Decimal

from django.db.models import Count, F, Subquery, OuterRef, Case, When, Value, FloatField
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from hystocks.apps.market.models import ProductMarketPrice
from hystocks.apps.products.models import Product
from hystocks.apps.products.serializers import ProductSerializer, ProductWeeklyStatsSerializer


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

    @action(detail=False, methods=['get'])
    def weekly(self, request):
        last_week = int((timezone.now() - timedelta(days=7)).timestamp()) * 1000

        last_week_value = Subquery(ProductMarketPrice.objects.filter(product_id=OuterRef('pk'), close_time__gte=last_week).order_by("close_time").values("close")[:1])
        current_value = Subquery(ProductMarketPrice.objects.filter(product_id=OuterRef('pk')).order_by("-close_time").values("close")[:1])

        qs = Product.objects.annotate(
            last_week_value=last_week_value,
            current_value=current_value,
            change=Case(
                When(last_week_value=0, then=0),
                default=current_value * 100 / last_week_value-100,
                output_field=FloatField(),
            )
        ).exclude(change=0)

        return Response({
            "gainers": ProductWeeklyStatsSerializer(qs.order_by('-change')[:5], many=True).data,
            "losers": ProductWeeklyStatsSerializer(qs.order_by('change')[:5], many=True).data,
        })
