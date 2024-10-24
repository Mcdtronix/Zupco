
from django.db import models

class Bus(models.Model):
    name = models.CharField(max_length=100, )
    numberPlate = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.numberPlate}  {self.name}"

class TrackingDevice(models.Model):
    trackID = models.AutoField(primary_key=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='tracking_devices')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    error_code = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Device {self.trackID} on {self.bus.name}"
    
class BusTrackingDevice(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    trackID = models.ForeignKey(TrackingDevice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.bus.name} - Device {self.trackID.trackID}"