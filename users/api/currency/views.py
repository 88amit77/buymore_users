from rest_framework import viewsets
from .models import Currency
from .serializers import CurrencySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all().order_by('-created_at')
    serializer_class = CurrencySerializer
