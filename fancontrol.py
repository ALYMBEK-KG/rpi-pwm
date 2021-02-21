from time import sleep
import RPi.GPIO as GPIO

gpioPin = 14
onTemp = 60
offTemp = onTemp - 5
everySec = 5

def inititalize():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpioPin, GPIO.OUT)
    GPIO.setwarnings(False)
    return ()

def get_temp():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp_str = f.read()

    try:
        return int(temp_str) / 1000
    except (IndexError, ValueError,) as e:
        raise RuntimeError('Could not parse temperature output.') from e


try:
    inititalize()
    while True:
        temp = get_temp()
        if temp > onTemp:
            GPIO.output(gpioPin, True)
        elif temp < offTemp:
            GPIO.output(gpioPin, False)
        sleep(everySec)
except KeyboardInterrupt:
    GPIO.cleanup()
