#Simulation of a pendulum, graphs position, velocity, and acceleration vs. time using meters and seconds
# Created by: Grant Smith and Patrick Wright

import math
import numpy as np 
import matplotlib.pyplot as plt
import csv 

#global variables

test_number = '1' #which number test is being performed
length = .226 # length in meters
timeinitial = 0 #time starting value
timefinal = 5  #ending time value
timestep = 0.001  #the 'dt' or how big each time step is 
mangle = (math.pi/12) # max (starting) angle in rads
a = 0 

        #variables for naming simulation test csv files, don't change
data = 'data'
L = 'L='
csv.p = '.csv'
testing = 'test'
file_name = testing + data + test_number + L + str(length) + csv.p

#defintion of functions

def print_system(time,pos,vel,accl):
    '''Prints the position ,velocity, and acceleration
    '''
    print("TIME:     ", round(time,5), ' s')
    print("POSITION: ", pos , ' degrees')
    print("VELOCITY: ", vel, ' m/s')
    print("ACCELERATION: ", accl, 'm/s^2', "\n")


def position(t):
    '''returns position of pendulum at given time t
    '''
    sr = (9.8)/(length)
    shift = (math.pi)/(2)
    sin = math.sqrt(sr)*t-shift
    rads = mangle * math.sin(sin) #position in radians
    pos =rads*(180/math.pi) #position in degerees
    return pos

def velocity(t):
    '''returns the veloctiy of pendulum at given time t
    '''
    vel = (position(t) - position(t-timestep))/timestep
    return vel

def acceleration(t):
    '''returns the acceleration of a pendulum at given time t
    '''
    accl = (velocity(t) - velocity(t - timestep))/timestep
    return accl


def movement():
    '''returns steps in time starting at time = 0 and ending at time = 1 with time step of .001 seconds
    '''
    time = 0
    time_end = 5
    while time <= time_end:
        print_system(time, position(time), velocity(time), acceleration(time))
        time += timestep # <--------how large step forward in time

def write_csv_data_file():
    time = 0
    time_end = 10
    csvData = [[]]
    while time <= time_end:
        csvData.append([time*1000, (acceleration(time))]) # look here ------------11-1-1-1-1-1
        time += timestep
    return csvData

def write_csv(data):
    with open(file_name, 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(data)

    csvFile.close()

def plotposition():
    '''returns plot of position vs time
    '''
    # Generate time list (x axis):
    a = 0
    timelist = []
    while a*timestep < timefinal:
        timelist.append(timeinitial+(a*timestep))
        a += 1
    poslist = []
    a = 0
    while a*timestep < timefinal:
        poslist.append(position(timeinitial+(a*timestep)))
        a += 1
    plt.subplot(3,1,2)
    plt.plot(timelist, poslist)
    plt.ylabel('Position(m)')
    plt.xlabel('Time(s)')
    plt.grid()
    plt.show()

def plotvelocity():
    '''returns plot of velocity vs time
    '''
    # Generate time list (x axis):
    a = 0
    timelist = []
    while a*timestep < timefinal:
        timelist.append(timeinitial+(a*timestep))
        a += 1
    vellist = []
    a = 0
    while a*timestep < timefinal:
        vellist.append(velocity(timeinitial+(a*timestep)))
        a += 1
    plt.subplot(3,1,2)
    plt.plot(timelist, vellist)
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time(s)')
    plt.grid()
    plt.show()

def plotacceleration():
    '''returns plot of acceleration vs time
    '''
    # Generate time list (x axis):
    a = 0
    timelist = []
    while a*timestep < timefinal:
        timelist.append(timeinitial+(a*timestep))
        a += 1
    accllist = []
    a = 0
    while a*timestep < timefinal:
        accllist.append(acceleration(timeinitial+(a*timestep)))
        a += 1
    plt.subplot(3,1,2)
    plt.plot(timelist, accllist)
    plt.ylabel('Acceleration (m/s^2)')
    plt.xlabel('Time(s)')
    plt.grid()
    plt.show()

#Script that gives position velocity and acceleration plot along with steping throught time
#at a time step = 0.001 s

row = write_csv_data_file()
plotposition()
plotvelocity()
plotacceleration()
movement()
write_csv(row)