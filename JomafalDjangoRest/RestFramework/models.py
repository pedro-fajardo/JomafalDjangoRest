from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phoneNumber = models.IntegerField()
    postalCode = models.TextField()

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
   documentNumber = models.TextField()
   warranty = models.BooleanField()
   client = models.ForeignKey(Client, related_name='equipments', on_delete=models.CASCADE)

   def __str__(self):
        return self.name
    