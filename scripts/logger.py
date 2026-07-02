import serial
import csv
import os
from datetime import datetime

# -----------------------------
# Configuration
# -----------------------------

PORT = "COM4"          # Change this
BAUD_RATE = 115200

CSV_FILE = "sensor_data.csv"

# -----------------------------
# Connect Serial
# -----------------------------

ser = serial.Serial(PORT, BAUD_RATE, timeout=1)

print("Connected to ESP32...")

# -----------------------------
# Create CSV
# -----------------------------

if not os.path.exists(CSV_FILE):

    with open(CSV_FILE, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Timestamp",
            "Temperature",
            "Humidity"
        ])

print("Logging Started...\n")

# -----------------------------
# Main Loop
# -----------------------------

while True:

    try:

        line = ser.readline().decode().strip()

        if line == "":
            continue

        if line == "ERROR":
            continue

        if line == "Temperature,Humidity":
            continue

        temperature, humidity = line.split(",")

        timestamp = datetime.now()

        with open(CSV_FILE, "a", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                timestamp,
                float(temperature),
                float(humidity)
            ])

        print(
            f"{timestamp}  "
            f"T={temperature}°C  "
            f"H={humidity}%"
        )

    except Exception as e:

        print(e)