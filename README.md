Zupco Bus Tracking System

This repository contains the code for a real-time bus tracking system for Zupco, Zimbabwe's public transport operator. The system utilizes an ESP32 microcontroller with a Neo6m GPS module to track bus locations. This data is then transmitted to a Django application, which integrates with Google Maps API to display bus locations on a real-time map.

Key Features:

Real-time Bus Tracking: Accurate and up-to-date tracking of bus locations.

Bus Registration: Allows for easy registration of buses and linking them to their respective tracking devices.

User-friendly Interface: A Django-based web application provides an intuitive interface for system administrators and users.

Google Maps Integration: Visualizes bus locations on a dynamic Google Map.

ESP32 Microcontroller: Utilizes the versatile ESP32 for robust and cost-effective data acquisition.

Neo6m GPS Module: Provides accurate and reliable GPS positioning data.

System Architecture:

Hardware:
ESP32 Microcontroller
Neo6m GPS Module
Cellular Communication Module (e.g., SIM800L) for data transmission

Software:
ESP32 Firmware:
Reads GPS data from the Neo6m module.
Transmits GPS coordinates and other relevant data (e.g., bus ID) to the server via the cellular module.

Django Application:
Receives and processes data from the ESP32.
Stores bus locations in a database.
Provides APIs for data retrieval and map display.
Generates the user interface for system administration and user interaction.

Google Maps API:
Displays bus locations on an interactive map.
Provides features like zooming, panning, and route visualization.
