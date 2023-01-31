import django_filters.rest_framework
from django_filters import DateFromToRangeFilter, rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementFilter(rest_framework.FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'status', 'creator', 'created_at']


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    filterset_fields = ["created_at", "creator"]

    def perfom_create(self, serializer):
        serializer.save(creator=self.request.creator)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
