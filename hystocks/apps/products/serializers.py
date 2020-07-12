from rest_framework import serializers

from hystocks.apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "asset_id",
            "name",
            "slug",
        )
