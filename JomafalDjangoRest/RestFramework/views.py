from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Client, Equipment
from .serializers import ClientSerializer, EquipmentGetSerializer, EquipmentPostSerializer

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class EquipmentListCreate(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentPostSerializer

class EquipmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentGetSerializer
    
    def get(self, request, *args, **kwargs):
        # Handle GET requests
        pk = self.kwargs.get('pk')
        equipmentExists = Equipment.objects.filter(pk=pk).exists()

        if equipmentExists: 
            try:
                equipments = Equipment.objects.get(pk=pk)
            except Equipment.DoesNotExist:
                return Response({'error': 'Equipment not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            equipments = Equipment.objects.all()
            
        serializer = EquipmentGetSerializer(equipments, many=not equipmentExists)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Handle POST requests
        serializer = EquipmentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        # Handle PUT requests to update an existing equipment
        try:
            equipment = Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            return Response({'error': 'Equipment not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EquipmentPostSerializer(equipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EquipmentListRetrieve(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentGetSerializer
