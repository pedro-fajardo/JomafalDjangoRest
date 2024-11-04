from django.urls import path
from .views import ClientListCreate, ClientRetrieveUpdateDestroy, EquipmentRetrieveUpdateDestroy, EquipmentListView

urlpatterns = [
   path('clients/', ClientListCreate.as_view(), name='client-list-create'),
   path('client/<int:pk>/', ClientRetrieveUpdateDestroy.as_view(), name='client-detail'),
   path('equipment/<int:pk>/', EquipmentRetrieveUpdateDestroy.as_view(), name='equipment-detail'),
   path('equipments/', EquipmentListView.as_view(), name='equipment-list'),
]