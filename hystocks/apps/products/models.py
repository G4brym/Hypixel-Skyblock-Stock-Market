from django.db import models

from hystocks.apps.core.models import Timestamped


class Product(Timestamped):
    asset_id = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128)


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)

    # Sell
    sell_price = models.DecimalField(max_digits=32, decimal_places=4)
    sell_volume = models.BigIntegerField()
    sell_orders = models.BigIntegerField()

    # Buy
    buy_price = models.DecimalField(max_digits=32, decimal_places=4)
    buy_volume = models.BigIntegerField()
    buy_orders = models.BigIntegerField()

    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
