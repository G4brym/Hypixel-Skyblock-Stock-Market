from django.db import models

from hystocks.apps.products.models import Product


class ProductMarketPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name="market")

    open_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    open = models.DecimalField(max_digits=32, decimal_places=4)
    high = models.DecimalField(max_digits=32, decimal_places=4)
    low = models.DecimalField(max_digits=32, decimal_places=4)
    close = models.DecimalField(max_digits=32, decimal_places=4)
    volume = models.BigIntegerField()
    close_time = models.DateTimeField(auto_now=False, auto_now_add=False)

