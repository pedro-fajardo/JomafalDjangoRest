from django.utils import timezone
from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phoneNumber = models.IntegerField()
    nif = models.IntegerField()
    postalCode = models.TextField()
    clientNumber = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
class Equipment(models.Model):
   name = models.CharField(max_length=100)
   productNumber = models.TextField()
   serialNumber = models.TextField()
   breakdown = models.TextField()
   observations = models.TextField()
   receivedDate = models.DateTimeField()
   status = models.TextField()
   documentNumber = models.TextField(null=True)
   warranty = models.BooleanField()
   warrantyDate = models.DateField(null=True)
   receiptNumber = models.IntegerField(null=True)
   client = models.ForeignKey(Client, related_name='equipments', on_delete=models.CASCADE)

   def __str__(self):
        return self.name
    