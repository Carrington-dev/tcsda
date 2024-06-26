from rest_framework.routers import DefaultRouter
from transact.views import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls