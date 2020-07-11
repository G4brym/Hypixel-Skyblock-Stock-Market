from rest_framework import routers

from hystocks.apps.market.viewsets import ProductMarketPriceViewSet

router = routers.SimpleRouter()
router.register('market', ProductMarketPriceViewSet)
