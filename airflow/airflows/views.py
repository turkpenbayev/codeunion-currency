from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated

from airflows.models import Currency
from airflows.serializers import CurrencySerializer


class CurrencyViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    
    serializer_class = CurrencySerializer
    permission_classes=[IsAuthenticated, ]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        return Currency.objects.all().order_by('pk')

