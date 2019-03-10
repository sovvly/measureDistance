import RPi.GPIO as GPIO
import time

# setup
GPIO.setmode(GPIO.BCM)
PIN_TRIGGER = 4
PIN_ECHO = 17
PIN_RED_LED = 22
PIN_YELLOW_LED = 23
PIN_GREEN_LED = 18

# connecting pins
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.setup(PIN_GREEN_LED, GPIO.OUT)
GPIO.setup(PIN_YELLOW_LED, GPIO.OUT)
GPIO.setup(PIN_RED_LED, GPIO.OUT)

while 1 == 1:
    time.sleep(1)
    GPIO.output(PIN_GREEN_LED, GPIO.LOW)
    GPIO.output(PIN_YELLOW_LED, GPIO.LOW)
    GPIO.output(PIN_RED_LED, GPIO.LOW)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    #reaching echo
    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()

    #calculation of distance
    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print("Distance:", distance, "cm")

    #bliking led
    if distance >= 30.00:
        GPIO.output(PIN_GREEN_LED, GPIO.HIGH)
    elif 30.00 > distance >= 10.00:
        GPIO.output(PIN_YELLOW_LED, GPIO.HIGH)
    else:
        GPIO.output(PIN_RED_LED, GPIO.HIGH)
