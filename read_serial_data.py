import os
import serial
import time
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bus_tracking.settings")
django.setup()

from Tracking.models import TrackingDevice, BusTrackingDevice

def main():
    # Open serial port
    ser = serial.Serial('COM13', 115200, timeout=1)
    time.sleep(2)  # Allow time for the serial connection to initialize

    latitude = None
    longitude = None
    error_code = None

    while True:
        line = ser.readline().decode('utf-8').strip()
        print(f"Raw data from serial: {line}")  # Debugging line

        if "Error code:" in line:
            error_code = line.split(": ")[1].strip()
            print(f"Error code detected: {error_code}")  # Print error code to terminal
        elif "Latitude:" in line:
            latitude = float(line.split(": ")[1].strip())
        elif "Longitude:" in line:
            longitude = float(line.split(": ")[1].strip())

            if latitude is not None and longitude is not None:
                try:
                    # Replace '1' with your actual bus ID or logic to get the correct bus
                    bus_id = 3
                    print(f"Trying to find BusTrackingDevice for bus_id={bus_id}")  # Debugging line

                    bus_tracking_device = BusTrackingDevice.objects.get(bus_id=bus_id)
                    tracking_device = bus_tracking_device.trackID

                    tracking_device.latitude = latitude
                    tracking_device.longitude = longitude
                    tracking_device.error_code = error_code
                    tracking_device.save()

                    print(f"Updated coordinates: latitude={latitude}, longitude={longitude}, error_code={error_code}")  # Debugging line

                except BusTrackingDevice.DoesNotExist:
                    print(f"BusTrackingDevice not found for bus_id={bus_id}.")  # More specific debugging message
                except Exception as e:
                    print(f"Error updating data: {e}")

                latitude = None
                longitude = None
                error_code = None

if __name__ == "__main__":
    main()
