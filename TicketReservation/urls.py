from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('ticket', TicketViewSet, basename='ticket')
router.register('order-item', OrderItemViewSet, basename='order-item')
router.register('order', OrderViewSet, basename='order')


urlpatterns=router.urls