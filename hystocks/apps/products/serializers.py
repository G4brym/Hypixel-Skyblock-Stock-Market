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


class ProductWeeklyStatsSerializer(serializers.ModelSerializer):
    change = serializers.SerializerMethodField()
    current_value = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "asset_id",
            "name",
            "slug",
            "change",
            "current_value",
        )

    def get_current_value(self, instance):
        return "%.2f" % instance.current_value

    def get_change(self, instance):
        return int(instance.change)
