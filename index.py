"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
import time
from adafruit_circuitplayground import cp
ledNumber = 9
while True:
    if ledNumber == -1:
        ledNumber = 9
    if ledNumber == 10:
        ledNumber = 0
    cp.pixels[ledNumber] = 1
    time.sleep(0.5)
    cp.pixels[ledNumber] =0
    if cp.switch:
        ledNumber += 1
    else:
        ledNumber -= 1
   
