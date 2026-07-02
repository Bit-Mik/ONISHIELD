import serial
import joblib
import time

PORT = "COM4"
BAUD = 115200

model = joblib.load("blower_model.pkl")

ser = serial.Serial(PORT, BAUD)

print("Connected...")

while True:

    try:

        line = ser.readline().decode().strip()

        if line == "":
            continue

        if line == "ERROR":
            continue

        if line == "ONI_SHIELD_STARTED":
            print(line)
            continue

        temp, hum = map(float, line.split(","))

        prediction = model.predict([[temp, hum]])

        blower = int(prediction[0])

        blower = max(
            0,
            min(
                blower,
                100
            )
        )

        ser.write(
            f"{blower}\n".encode()
        )

        print(
            f"T={temp}  H={hum}  Fan={blower}%"
        )

    except Exception as e:

        print(e)