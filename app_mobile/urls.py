from django.urls import path
from rest_framework.routers import DefaultRouter

from app_mobile.views import WordGroupViewSet, HomonymViewSet

router = DefaultRouter()
router.register(r'wordgroups', WordGroupViewSet)
router.register(r'homonym', HomonymViewSet)

urlpatterns = router.urls
