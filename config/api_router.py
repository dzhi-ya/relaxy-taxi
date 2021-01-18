from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from relaxy_taxi.main.api.views import CarViewSet, OrderViewSet
from relaxy_taxi.users.api.views import UserViewSet, ClientViewSet, DriverViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("clients", ClientViewSet)
router.register("drivers", DriverViewSet)
router.register("cars", CarViewSet)
router.register("orders", OrderViewSet)

app_name = "api"
urlpatterns = router.urls
