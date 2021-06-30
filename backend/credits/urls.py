""" Credits urls. """

from .views import CreditModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'credits', CreditModelViewSet, basename='credits')
urlpatterns = router.urls