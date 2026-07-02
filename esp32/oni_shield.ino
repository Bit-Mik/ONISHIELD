#include "config.h"
#include "dht_sensor.h"
#include "blower_control.h"

float temperature;
float humidity;

int blowerSpeed = 0;

void setup()
{
    Serial.begin(115200);

    initSensor();

    initBlower();

    Serial.println("ONI_SHIELD_STARTED");
}

void loop()
{
    temperature = getTemperature();
    humidity = getHumidity();

    if (isnan(temperature) || isnan(humidity))
    {
        Serial.println("ERROR");
        delay(SENSOR_DELAY);
        return;
    }

    // Send sensor data to Python
    Serial.print(temperature);
    Serial.print(",");
    Serial.println(humidity);

    // Wait for prediction
    unsigned long start = millis();

    while (!Serial.available())
    {
        if (millis() - start > 1000)
            break;
    }

    if (Serial.available())
    {
        blowerSpeed = Serial.parseInt();

        blowerSpeed = constrain(
            blowerSpeed,
            0,
            100
        );

        setBlowerSpeed(blowerSpeed);

        Serial.print("Fan : ");
        Serial.print(blowerSpeed);
        Serial.println("%");
    }

    delay(SENSOR_DELAY);
}