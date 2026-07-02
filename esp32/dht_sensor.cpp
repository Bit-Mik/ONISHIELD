#include <Arduino.h>
#include <DHT.h>

#include "config.h"
#include "dht_sensor.h"

DHT dht(DHT_PIN, DHT_TYPE);

void initSensor()
{
    dht.begin();
}

float getTemperature()
{
    return dht.readTemperature();
}

float getHumidity()
{
    return dht.readHumidity();
}