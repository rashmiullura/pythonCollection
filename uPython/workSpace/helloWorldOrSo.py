# copied from https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    sleep(0.05) # discoooo!

