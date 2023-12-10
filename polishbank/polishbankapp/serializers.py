from rest_framework import serializers
from .models import PolishBank

class PolishBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolishBank
        fields = '__all__'
