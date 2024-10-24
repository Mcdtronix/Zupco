#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from django.core.management import call_command
from threading import Thread
import os
import sys

def run_serial_data():
    call_command('run_serial_data')


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bus_tracking.settings")

    from django.core.management import execute_from_command_line

    # Start the serial data command in a separate thread
    serial_thread = Thread(target=run_serial_data)
    serial_thread.start()

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
