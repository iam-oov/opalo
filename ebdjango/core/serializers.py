from rest_framework import serializers

from core import models as mod_core


class MarketModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = mod_core.Market
        fields = '__all__'
