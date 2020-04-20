from rest_framework import viewsets
from .models import Currency
from .serializers import CurrencySerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all().order_by('-created_at')
    serializer_class = CurrencySerializer


class CurrencyFilterView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        qs = Currency.objects.all().order_by('currency_name')
        if 'id' in request.data:
            ids = request.data['id'].split(',')
            qs = qs.filter(id__in=ids)
        if 'currency' in request.data:
            qs = qs.filter(currency_name__contains=request.data['currency'])
        currencies = [{currency.currency_name: currency.currency_name} for currency in qs]
        return Response(currencies)


class CurrencyIdFilterView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        qs = Currency.objects.all().order_by('id')
        if 'id' in request.data:
            ids = request.data['id'].split(',')
            qs = qs.filter(id__in=ids)
        if 'currency' in request.data:
            currency_names = request.data['currency'].split(',')
            qs = qs.filter(currency_name__in=currency_names)
        currencies = [{currency.id: currency.id} for currency in qs]
        return Response(currencies)


class CurrencyKeywordFilterView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        qs = Currency.objects.all().order_by('id')
        if 'id' in request.data:
            ids = request.data['id'].split(',')
            qs = qs.filter(id__in=ids)
        if 'keyword' in request.data:
            qs = qs.filter(currency_name__contains=request.data['keyword'])
        currencies = [{currency.id: currency.id} for currency in qs]
        return Response(currencies)
