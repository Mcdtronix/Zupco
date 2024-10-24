
from django.contrib import admin
from .models import Bus, TrackingDevice,BusTrackingDevice

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'numberPlate')

@admin.register(TrackingDevice)
class TrackingDeviceAdmin(admin.ModelAdmin):
    list_display = ('trackID', 'bus', 'latitude', 'longitude', 'timestamp')
    readonly_fields = ('trackID', 'latitude', 'longitude', 'timestamp')

@admin.register(BusTrackingDevice)
class BusTrackingDeviceAdmin(admin.ModelAdmin):
    list_display = ('bus', 'trackID')
    