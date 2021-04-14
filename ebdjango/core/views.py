from rest_framework import viewsets

from core import serializers as ser_core
from core import models as mod_core


class MarketViewSet(viewsets.ModelViewSet):
    queryset = mod_core.Market.objects.all()
    serializer_class = ser_core.MarketModelSerializer
