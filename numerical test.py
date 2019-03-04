import math
import numpy as np 
import matplotlib.pyplot as plt 


timeinitial = 0 #IMPORTANT
timefinal = 5
timestep = 0.001 # IMPORTANT
length = 1 #IMPORTANT, length in meters
mangle = (math.pi/12) # max (starting) angle in rads
a = 0 #don't touch this

def print_system(time,pos,vel,accl):
    print("TIME:     ", round(time,2), ' s')
    print("POSITION: ", pos , ' degrees')
    print("VELOCITY: ", vel, ' m/s')
    print("ACCELERATION: ", accl, 'm/s^2', "\n")


def position(t):
    sr = (9.8)/(length)
    shift = (math.pi)/(2)
    sin = math.sqrt(sr)*t-shift
    rads = mangle * math.sin(sin) #position in radians
    pos =rads*(180/math.pi) #position in degerees
    return pos

def velocity(t):
    vel = (position(t) - position(t-timestep))/timestep
    return vel

def acceleration(t):
    accl = (velocity(t) - velocity(t - timestep))/timestep
    return accl

def movement():
    time = 0
    time_end = 1
    while time <= time_end:
        print_system(time, position(time), velocity(time), acceleration(time))
        time += timestep # <--------how large step forward in time

def plotposition():
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
    plt.ylabel('Acceleration (m/s)')
    plt.xlabel('Time(s)')
    plt.grid()
    plt.show()

plotposition()
plotvelocity()
plotacceleration()