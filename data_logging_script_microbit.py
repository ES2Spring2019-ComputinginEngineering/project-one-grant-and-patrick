#Logs accelerometer values of the microbit in the x, y, and z axies 
#Created by: Grant Smith and Patrick Wright

import microbit
import math

#global variables

toggle = 0
collectaccel = microbit.Image('00000:00000:09990:00000:00000')

#script that collects data
#press a to start data collection and press a again to end data collection

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
