from rest_framework.routers import DefaultRouter
from ArtsHub.views import ArtObjectViewSet
router = DefaultRouter()
router.register('artobjects', ArtObjectViewSet, basename='artobjects')
urlpatterns = router.urls