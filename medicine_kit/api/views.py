from rest_framework import viewsets

from .serializers import DrugSerializer, BoxSerializers
from preparations.models import Drug, Box
from .pagination import CustomPagination
from .filters import DrugSearchFilter


class DrugViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    filter_backends = (DrugSearchFilter,)
    pagination_class = CustomPagination
    search_fields = ('^name', )


class BoxViewSet(viewsets.ModelViewSet):

    queryset = Box.objects.all()
    serializer_class = BoxSerializers
