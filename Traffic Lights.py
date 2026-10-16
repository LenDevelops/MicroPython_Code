from machine import Pin
import time

ledr = Pin(15, Pin.OUT)
ledy = Pin(13, Pin.OUT)
ledg = Pin(12, Pin.OUT)

ledr.value(0)
ledy.value(0)
ledg.value(0)

while True:
    ledr.value(0)
    ledy.value(0)
    ledg.value(1)
    time.sleep(3)
    
    ledy.value(1)
    ledg.value(0)
    time.sleep(1)
    
    ledr.value(1)
    ledy.value(0)
    time.sleep(3)
    
    ledy.value(1)
    time.sleep(1)