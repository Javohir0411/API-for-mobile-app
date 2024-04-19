from django_filters import FilterSet, rest_framework as filters
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

from app_mobile.models import WordGroup, Homonym
from app_mobile.permissions import MyPermissions
from app_mobile.serializers import (
    WordGroupSerializer,
    HomonymListSerializer,
    HomonymAllInfoSerializer
)


class WordGroupViewSet(viewsets.ModelViewSet):
    queryset = WordGroup.objects.all()
    serializer_class = WordGroupSerializer
    permission_classes = [MyPermissions]


# BU IKKINCHI VARIANT QILIB YOZIB QO'YILDI
# class HomonymListAPIView(ListAPIView):
#     queryset = Homonym.objects.all()
#     serializer_class = HomonymListSerializer
#     filter_backends = [filters.DjangoFilterBackend]
#     filterset_fields = ['homonym_name']

# # BU IKKINCHI VARIANT QILIB YOZIB QO'YILDI
# class HomonymDetailAPIView(RetrieveAPIView):
#     queryset = Homonym.objects.all()
#     serializer_class = HomonymAllInfoSerializer


class HomonymViewSet(viewsets.ModelViewSet):
    queryset = Homonym.objects.all()
    permission_classes = [MyPermissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return HomonymListSerializer
        else:
            return HomonymAllInfoSerializer

#filter uchun
# class HomonymFilter(FilterSet):
#     class Meta:
#         model = Homonym
#         fields = ['homonym_name']
