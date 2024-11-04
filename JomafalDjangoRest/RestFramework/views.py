from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Client, Equipment, EquipmentPart
from .serializers import ClientSerializer, EquipmentSerializer, EquipmentPostSerializer

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class EquipmentListView(APIView):
    def get(self, request):
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EquipmentPostSerializer(data=request.data)
        if serializer.is_valid():
            equipment = serializer.save()
            response_serializer = EquipmentPostSerializer(equipment)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EquipmentRetrieveUpdateDestroy(APIView):    
    def get(self, request, pk):
        try:
            equipment = Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            equipment = Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipment not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EquipmentSerializer(equipment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            equipment = Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipment not found"}, status=status.HTTP_404_NOT_FOUND)

        equipment.delete()
        return Response({"message": "Equipment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)