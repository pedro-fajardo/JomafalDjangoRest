from rest_framework import serializers
from .models import Client, Equipment

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class EquipmentGetSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    
    class Meta:
        model = Equipment
        fields = '__all__'

class EquipmentPostSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Equipment
        fields = '__all__'