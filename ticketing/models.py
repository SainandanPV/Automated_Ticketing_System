# myapp/models.py

from django.db import models
from django.contrib.auth.models import User
import requests

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
        origin=f"{self.start_latitude},{self.start_longitude}"
        destination=f"{self.end_latitude},{self.end_longitude}"
        google_maps_api_key='AIzaSyBtOUAH8tyxMwEGLMxmRPoYBhGRS3zaOlc'
        url=f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={google_maps_api_key}"

        response=requests.get(url)
        directions_data=response.json()

        if directions_data['status']=='OK':
            route=directions_data['routes'][0]
            leg=route['legs'][0]
            distance=leg['distance']['value']
            return distance/1000
        else:
            return None

    
    def calculate_amount(self):
        distance=self.calculate_distance()
        return distance*1.5

