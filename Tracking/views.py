from django.shortcuts import render
from .models import Bus, TrackingDevice, BusTrackingDevice
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def map_view(request):
    devices = TrackingDevice.objects.all()
    buses = Bus.objects.all()  
    context = {
        'devices': devices,
        'buses': buses
    }
    return render(request, 'tracking/map.html', context)


def update_gps_data(request, bus_id):
    try:
        # Fetch tracking devices for the specified bus_id
        bus_tracking_devices = BusTrackingDevice.objects.filter(bus_id=bus_id).select_related('trackID')

        # If no devices found, return an error
        if not bus_tracking_devices.exists():
            return JsonResponse({'status': 'error', 'message': 'BusTrackingDevice not found'}, status=404)

        # Prepare data to return
        device_data = []
        for bus_tracking_device in bus_tracking_devices:
            tracking_device = bus_tracking_device.trackID
            device_data.append({
                'latitude': tracking_device.latitude,
                'longitude': tracking_device.longitude,
                'bus': {
                    'name': tracking_device.bus.name
                }
            })

        # Assuming you want to return the first device's data as context
        if device_data:
            context = {'latitude': device_data[0]['latitude'], 'longitude': device_data[0]['longitude']}
        else:
            context = {}

        # Return a success response with data
        return JsonResponse({'status': 'success', 'data': context})

    except Exception as e:
        # Handle any unexpected errors
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
