from rest_framework import serializers
from airflows.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
      model = Currency
      fields = ('id', 'name', 'rate')
      read_only_fields = fields