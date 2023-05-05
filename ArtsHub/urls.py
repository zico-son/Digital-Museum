from rest_framework.routers import DefaultRouter
from ArtsHub.views import ArtObjectViewSet, HallViewSet
router = DefaultRouter()
router.register('artobjects', ArtObjectViewSet, basename='artobjects')
router.register('halls', HallViewSet, basename='halls')
urlpatterns = router.urls