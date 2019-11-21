from rest_framework.routers import DefaultRouter
from orders import viewsets as complete_pc_views

router = DefaultRouter()
router.register('orders', complete_pc_views.CompletePcViewSet, base_name='order')
