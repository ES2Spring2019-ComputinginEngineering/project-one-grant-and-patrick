import math

def print_system(time,pos,vel,accl):
    print("TIME:     ", time, ' s')
    print("POSITION: ", pos , ' rads')
    print("VELOCITY: ", vel, ' m/s')
    print("ACCELERATION: ", accl, 'm/s^2', "\n")

def time():


def position(t):
    mangle = (math.pi/12)
    sr = (9.8)/(.1)
    shift = (9.8)/(.1)
    sin = math.sqrt(sr)*t-shift
    pos = mangle * math.sin(sin)

def velocity(t):


def acceleration():
