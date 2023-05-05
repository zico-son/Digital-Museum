from rest_framework.viewsets import ReadOnlyModelViewSet
from ArtsHub.models import ArtObject, Hall
from ArtsHub.serializers import ArtObjectSerializer, HallSerializer
from ArtsHub.pagination import CustomPagination
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
class ArtObjectViewSet(ReadOnlyModelViewSet):
    pagination_class = CustomPagination
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['hall__name', 'epoch', 'active', 'highlighted']
    search_fields = ['name', 'art_story__title','epoch', 'hall__name']
    queryset = ArtObject.objects \
        .select_related('hall') \
        .prefetch_related('images') \
        .prefetch_related('holdings') \
        .select_related('art_story') \
        .select_related('chariot') \
        .select_related('painting') \
        .select_related('other') \
        .select_related('borrowed_collection') \
        .select_related('permanent_collection') \
        .all()
    serializer_class = ArtObjectSerializer

class HallViewSet(ReadOnlyModelViewSet):
    pagination_class = CustomPagination
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['name']
    queryset = Hall.objects.all()
    serializer_class = HallSerializer