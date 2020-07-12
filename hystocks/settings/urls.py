from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from hystocks.apps.core.views import VuejsView
from hystocks.apps.market.viewsets import ProductMarketPriceViewSet
from hystocks.apps.products.viewsets import ProductViewSet

router = SimpleRouter()
router.register("products", ProductViewSet)
router.register("market", ProductMarketPriceViewSet)

urlpatterns = [
    # Vuejs view
    path("", VuejsView.as_view(), name="index"),

    # Internal api
    path("api/v1/", include(router.urls),),
]

if settings.DEBUG:
    import debug_toolbar
    from django.contrib import admin

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
