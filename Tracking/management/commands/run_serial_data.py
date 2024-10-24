from django.core.management.base import BaseCommand
import serial
import time
from Tracking.models import TrackingDevice, BusTrackingDevice

class Command(BaseCommand):
    help = 'Reads serial data and updates GPS coordinates'

    def handle(self, *args, **options):
        ser = serial.Serial('COM13', 115200, timeout=1)
        time.sleep(2)  # Allow time for the serial connection to initialize
        latitude = None
        longitude = None
        error_code = None

        while True:
            line = ser.readline().decode('utf-8').strip()
            self.stdout.write(f"Raw data from serial: {line}")

            if "Error code:" in line:
                error_code = line.split(": ")[1].strip()
                self.stdout.write(f"Error code detected: {error_code}")
            elif "Latitude:" in line:
                latitude = float(line.split(": ")[1].strip())
            elif "Longitude:" in line:
                longitude = float(line.split(": ")[1].strip())

                if latitude is not None and longitude is not None:
                    try:
                        bus_tracking_device = BusTrackingDevice.objects.get(bus_id=1)  # Replace with actual bus ID or logic
                        tracking_device = bus_tracking_device.trackID

                        tracking_device.latitude = latitude
                        tracking_device.longitude = longitude
                        tracking_device.error_code = error_code
                        tracking_device.save()

                        self.stdout.write(f"Updated coordinates: latitude={latitude}, longitude={longitude}, error_code={error_code}")
                    except BusTrackingDevice.DoesNotExist:
                        self.stdout.write("BusTrackingDevice not found for the specified bus.")
                    except Exception as e:
                        self.stdout.write(f"Error updating data: {e}")

                    latitude = None
                    longitude = None
                    error_code = None
