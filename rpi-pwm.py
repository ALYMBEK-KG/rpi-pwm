from time import sleep
import RPi.GPIO as GPIO

class RpiPwm:
  delay = 5
  gpio = 14
  on = 75
  off = on - 5

  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.gpio, GPIO.OUT)
    GPIO.setwarnings(False)

    try:
      while True:
        self.run()
        sleep(self.delay)
    except KeyboardInterrupt:
      GPIO.cleanup()

  def get_temp(self):
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
      temp_str = f.read()

    try:
      return int(temp_str) / 1000
    except (IndexError, ValueError) as e:
      raise RuntimeError('Could not parse temperature output') from e

  def run(self):
    temp = self.get_temp()

    if temp > self.on:
      GPIO.output(self.gpio, True)
    elif temp < self.off:
      GPIO.output(self.gpio, False)


RpiPwm()
