from rest_framework import routers
from automation_store.core.views import ShirtViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"shirt", ShirtViewSet, basename="shirt")
