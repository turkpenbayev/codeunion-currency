from rest_framework import routers

from airflows.views import CurrencyViewSet

router = routers.DefaultRouter()
router.register('currencies', CurrencyViewSet, basename='currencies')

urlpatterns = router.urls
