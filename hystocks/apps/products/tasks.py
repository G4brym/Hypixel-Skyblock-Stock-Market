import json

import requests
from django.conf import settings
from django.utils.datetime_safe import datetime
from django.utils.timezone import make_aware

from hystocks.apps.products.models import Product, ProductPrice
from hystocks.settings.celery import app


@app.task(ignore_result=True)
def crawl_products_prices():
    print("#TASK: Running Products Crawl")

    data = requests.get("https://api.hypixel.net/skyblock/bazaar?key={}".format(settings.HYPIXEL_API_KEY))
    data = json.loads(data.content)

    if data["success"] is not True:
        raise RuntimeError("API returned Success False!")

    data_time = make_aware(datetime.fromtimestamp(data["lastUpdated"]/1000))

    products = {
        prod.asset_id: prod
        for prod in Product.objects.all()
    }

    bulk_prices = []
    for product in data["products"].values():
        if product["product_id"] not in products.keys():
            _prod = Product.objects.create(asset_id=product["product_id"])
            products[_prod.asset_id] = _prod

        bulk_prices.append(ProductPrice(
            product=products[product["product_id"]],
            sell_price=product["quick_status"]["sellPrice"],
            sell_volume=product["quick_status"]["sellVolume"],
            sell_orders=product["quick_status"]["sellOrders"],
            buy_price=product["quick_status"]["buyPrice"],
            buy_volume=product["quick_status"]["buyVolume"],
            buy_orders=product["quick_status"]["buyOrders"],
            created_at=data_time,
        ))

    ProductPrice.objects.bulk_create(bulk_prices)

    print("Finished crawl")
