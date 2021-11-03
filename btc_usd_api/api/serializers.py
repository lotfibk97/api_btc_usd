from rest_framework.serializers import ModelSerializer
from .models import RealTimeRate
from django.conf import settings

class RealTimeRateSerializer(ModelSerializer):
    def create(self, validated_data):
        return RealTimeRate.objects.create(**validated_data)
    class Meta:
        model = RealTimeRate
        fields = ('from_currency_code', 'from_currency_name', 'to_currency_code',
         'to_currency_name', 'exchange_rate', 'last_refreshed', 'time_zone', 
         'bid_price', 'ask_price')
