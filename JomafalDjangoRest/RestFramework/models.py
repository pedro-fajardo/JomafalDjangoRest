from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    phoneNumber = models.TextField(null=True, blank=True)
    nif = models.TextField(null=True, blank=True)
    postalCode = models.TextField(null=True, blank=True)
    clientNumber = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    productNumber = models.TextField(null=True, blank=True)
    serialNumber = models.TextField(null=True, blank=True)
    breakdown = models.TextField(null=True, blank=True)
    observations = models.TextField(null=True, blank=True)
    receivedDate = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    documentNumber = models.TextField(null=True, blank=True)
    warranty = models.BooleanField(null=True, blank=True)
    warrantyDate = models.TextField(null=True, blank=True)
    receiptNumber = models.TextField(null=True, blank=True)
    partsIva = models.TextField(null=True, blank=True)
    client = models.ForeignKey(Client, related_name='equipments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class EquipmentPart(models.Model):
    code = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    value = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    equipment = models.ForeignKey(Equipment, related_name='parts', on_delete=models.CASCADE)  # Add this line

    def __str__(self):
        return self.code
   
