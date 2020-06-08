import json
from datetime import datetime

import requests
from django.conf import settings

from hystocks.apps.products.models import Product, ProductPrice
from hystocks.settings.celery import app


@app.task(ignore_result=True)
def crawl_products_prices():
    print("#TASK: Running Products Crawl")

    data = requests.get("https://api.hypixel.net/skyblock/bazaar?key={}".format(settings.HYPIXEL_API_KEY))
    data = json.loads(data.content)

    if data["success"] is not True:
        raise RuntimeError("API returned Success False!")

    data_time = datetime.fromtimestamp(data["lastUpdated"]/1000)

    products = {
        prod.asset_id: prod
        for prod in Product.objects.all()
    }

    bulk_prices = []
    for product in data["products"]:
        bulk_prices.append(ProductPrice(
            open_time=make_aware(datetime.fromtimestamp(price[0] / 1000)),
            open=price[1],
            high=price[2],
            low=price[3],
            close=price[4],
            volume=price[5],
            close_time=make_aware(datetime.fromtimestamp(price[6] / 1000)),
            quote_asset_volume=price[7],
            trades=price[8],
            taker_buy_base_asset_volume=price[9],
            taker_buy_quote_asset_volume=price[10],
            coin_id=coin.pk
        ))

    ProductPrice.objects.bulk_create(bulk_prices)

    # for coin in Coin.objects.all():
    #     last_price = coin.prices.order_by('-open_time').first()
    #     if last_price:
    #         _open_time = str(last_price.open_time.timestamp() * 1000)
    #
    #         prices = bclient.get_historical_klines(coin.flat_symbol, KLINE_INTERVAL_15MINUTE, start_str=_open_time, limit=1000)
    #     else:
    #         prices = bclient.get_klines(symbol=coin.flat_symbol, interval=KLINE_INTERVAL_15MINUTE, limit=1000)
    #
    #     bulk_prices = []
    #     # Create all prices except last
    #     for price in prices[1:]:
    #         bulk_prices.append(CoinPrice(
    #             open_time=make_aware(datetime.fromtimestamp(price[0] / 1000)),
    #             open=price[1],
    #             high=price[2],
    #             low=price[3],
    #             close=price[4],
    #             volume=price[5],
    #             close_time=make_aware(datetime.fromtimestamp(price[6] / 1000)),
    #             quote_asset_volume=price[7],
    #             trades=price[8],
    #             taker_buy_base_asset_volume=price[9],
    #             taker_buy_quote_asset_volume=price[10],
    #             coin_id=coin.pk
    #         ))
    #
    #     CoinPrice.objects.bulk_create(bulk_prices)
    #
    #     _last_bin = prices[0]
    #     _obj,_ = CoinPrice.objects.update_or_create(
    #         coin_id=coin.pk,
    #         open_time=make_aware(datetime.fromtimestamp(_last_bin[0] / 1000)),
    #         defaults={
    #             "open": _last_bin[1],
    #             "high": _last_bin[2],
    #             "low": _last_bin[3],
    #             "close": _last_bin[4],
    #             "volume": _last_bin[5],
    #             "close_time": make_aware(datetime.fromtimestamp(_last_bin[6] / 1000)),
    #             "quote_asset_volume": _last_bin[7],
    #             "trades": _last_bin[8],
    #             "taker_buy_base_asset_volume": _last_bin[9],
    #             "taker_buy_quote_asset_volume": _last_bin[10]
    #         }
    #     )
    #
    #     update_coin_percentages(coin, _obj)
    #
    #     # We dont count the last one because is always an update
    #     _loaded_prices += len(bulk_prices)

    print("Finished crawl")
