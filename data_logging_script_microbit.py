#Data Logging -- MicroBit
# Logs accelerometer values of the microbit in the x, y, and z axies 
#Created by: Grant Smith and Patrick Wright

#Press the A button to start data collection then press the A button once more to end the data collection.
#This will return a file named 'csvfile.txt' into your microbit and then drag and drop from microbit into your computer.

import microbit
import math

#global variables

toggle = 0
collectaccel = microbit.Image('00000:00000:09990:00000:00000')

#script that collects data

while toggle == 0:
    if microbit.button_a.is_pressed() == True:
        toggle = 1
        microbit.sleep(200)
        
with open('csvfile.txt', 'w') as datafile:
    while toggle == 1:
        microbit.display.show(collectaccel)
        microbit.sleep(10)
        x = microbit.accelerometer.get_x()
        y = microbit.accelerometer.get_y()
        z = microbit.accelerometer.get_z()
        datafile.write('('+str(x)+','+str(y)+','+str(z)+')')
        datafile.write("\n")
        if microbit.button_a.is_pressed() == True:
            microbit.display.clear()
            break
