from rest_framework import serializers
from .models import Client, Equipment, EquipmentPart

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class EquipmentPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentPart
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    parts = EquipmentPartSerializer(many=True, required=False)
    partsIva = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    class Meta:
        model = Equipment
        fields = '__all__'

    def create(self, validated_data):
        parts_data = validated_data.pop('parts', [])
        parts_iva = validated_data.get('partsIva', 0.0)  # Set a default if not provided
        equipment = Equipment.objects.create(partsIva=parts_iva, **validated_data)

        for part_data in parts_data:
            EquipmentPart.objects.create(equipment=equipment, **part_data)

        return equipment

    def update(self, instance, validated_data):
        parts_data = validated_data.pop('parts', [])

        # Update client if provided
        client_data = validated_data.pop('client', None)
        if client_data:
            client_serializer = ClientSerializer(instance.client, data=client_data)
            client_serializer.is_valid(raise_exception=True)
            client_serializer.save()

        # Update the Equipment instance fields
        instance.name = validated_data.get('name', instance.name)
        instance.productNumber = validated_data.get('productNumber', instance.productNumber)
        instance.serialNumber = validated_data.get('serialNumber', instance.serialNumber)
        instance.breakdown = validated_data.get('breakdown', instance.breakdown)
        instance.observations = validated_data.get('observations', instance.observations)
        instance.receivedDate = validated_data.get('receivedDate', instance.receivedDate)
        instance.status = validated_data.get('status', instance.status)
        instance.documentNumber = validated_data.get('documentNumber', instance.documentNumber)
        instance.warranty = validated_data.get('warranty', instance.warranty)
        instance.warrantyDate = validated_data.get('warrantyDate', instance.warrantyDate)
        instance.receiptNumber = validated_data.get('receiptNumber', instance.receiptNumber)
        instance.partsIva = validated_data.get('partsIva', instance.partsIva)
        instance.save()

        # Handle parts: update existing or create new
        existing_parts = instance.parts.all()
        existing_part_ids = {part.id: part for part in existing_parts}

        for part_data in parts_data:
            # Remove the equipment key if it exists
            part_data.pop('equipment', None)

            part_id = part_data.get('id', None)
            if part_id and part_id in existing_part_ids:
                # Update existing part
                part = existing_part_ids[part_id]
                part.code = part_data.get('code', part.code)
                part.quantity = part_data.get('quantity', part.quantity)
                part.description = part_data.get('description', part.description)
                part.value = part_data.get('value', part.value)
                part.save()
            else:
                # Create new part if it doesn't exist
                EquipmentPart.objects.create(equipment=instance, **part_data)

        # Optionally: remove parts that were not included in the update
        for existing_part in existing_parts:
            if existing_part.id not in [p.get('id') for p in parts_data]:
                existing_part.delete()  # Or mark as inactive, depending on your requirements

        return instance

class EquipmentPostSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), write_only=True)
    parts = EquipmentPartSerializer(many=True, required=False)

    class Meta:
        model = Equipment
        fields = '__all__'

    def create(self, validated_data):
        # Extract parts data
        parts_data = validated_data.pop('parts', [])
        
        # Extract client information
        client_object = validated_data.pop('client', None)

        # Retrieve the client instance; handle the case if client_id is None
        client = None
        if client_object:
            client_id = client_object.id  # Get the ID from the client object
            try:
                client = Client.objects.get(id=client_id)  # Fetch the client instance
            except Client.DoesNotExist:
                raise serializers.ValidationError({"client": "Client not found."})

        # Create the Equipment instance
        equipment = Equipment.objects.create(client=client, **validated_data)

        # Handle parts creation
        for part_data in parts_data:
            EquipmentPart.objects.create(equipment=equipment, **part_data)

        return equipment
