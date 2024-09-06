# The default ModelSerializer uses primary keys for relationships,
# but you can also easily generate nested represantations using the depth option
# Example
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name', 'balance']
        depth = 1
