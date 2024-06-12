from rest_framework import serializers

from .models import Accounts, Listeners, APIKeys


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'


class KeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKeys
        fields = '__all__'


class ListenersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listeners
        fields = '__all__'
