# myapp/models.py

from django.db import models
from django.contrib.auth.models import User
from geopy.distance import geodesic

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField(null=True)
    phone_number=models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.user.username

class RFIDCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid=models.CharField(max_length=30,unique=True,null=True) #UID for RFID card
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Card for {self.user.username}'
    
class RFIDCardLog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rfid_card=models.ForeignKey(RFIDCard,on_delete=models.CASCADE,null=True)
    start_latitude=models.DecimalField(max_digits=15, decimal_places=9)
    start_longitude=models.DecimalField(max_digits=15, decimal_places=6)
    end_latitude = models.DecimalField(max_digits=15, decimal_places=6)
    end_longitude = models.DecimalField(max_digits=15, decimal_places=6)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction for {self.rfid_card.uid} by {self.user.username}"
    
    def calculate_distance(self):
        start_location=(self.start_latitude,self.start_longitude)
        end_location = (self.end_latitude, self.end_longitude)

        return geodesic(start_location,end_location).kilometers
    
    def calculate_amount(self):
        distance=self.calculate_distance()
        return distance*1.5

