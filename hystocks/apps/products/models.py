from django.db import models
from django.utils.text import slugify

from hystocks.apps.core.models import Timestamped
from hystocks.apps.products.utils import get_name_from_asset_id


class Product(Timestamped):
    asset_id = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(max_length=128, null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = get_name_from_asset_id(self.asset_id)
        if not self.slug:
            self.slug = slugify(self.name)

        super(Product, self).save(*args, **kwargs)


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True, related_name="prices")

    # Sell
    sell_price = models.DecimalField(max_digits=32, decimal_places=4)
    sell_volume = models.BigIntegerField()
    sell_orders = models.BigIntegerField()

    # Buy
    buy_price = models.DecimalField(max_digits=32, decimal_places=4)
    buy_volume = models.BigIntegerField()
    buy_orders = models.BigIntegerField()

    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)

    @property
    def price(self):
        return self.sell_price
