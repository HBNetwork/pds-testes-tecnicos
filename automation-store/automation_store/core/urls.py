from rest_framework import routers
from .views import ShirtViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"shirt", ShirtViewSet, basename="shirt")
