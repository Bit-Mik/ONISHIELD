#include <Arduino.h>

#include "config.h"
#include "blower_control.h"

void initBlower()
{
    ledcSetup(
        FAN_PWM_CHANNEL,
        FAN_PWM_FREQ,
        FAN_PWM_RES
    );

    ledcAttachPin(
        FAN_PWM_PIN,
        FAN_PWM_CHANNEL
    );
}

void setBlowerSpeed(int percent)
{
    percent = constrain(percent,0,100);

    int pwm = map(
        percent,
        0,
        100,
        0,
        255
    );

    ledcWrite(
        FAN_PWM_CHANNEL,
        pwm
    );
}