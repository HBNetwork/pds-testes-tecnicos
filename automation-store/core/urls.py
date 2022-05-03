from rest_framework import routers
from .views import TshirtViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"tshirt", TshirtViewSet, basename="tshirt")
