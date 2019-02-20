import math

def print_system(time,pos,vel,accl):
    print("TIME:     ", time, ' s')
    print("POSITION: ", pos , ' degrees')
    print("VELOCITY: ", vel, ' m/s')
    print("ACCELERATION: ", accl, 'm/s^2', "\n")


def position(t):
    mangle = (math.pi/12)
    sr = (9.8)/(.1)
    shift = (math.pi)/(2)
    sin = math.sqrt(sr)*10-shift
    rads = mangle * math.sin(sin) #position in radians
    pos =rads*(180/math.pi) #position in degerees
    return pos

def velocity(t):
    #x
    v_x = 21*math.sin(7*math.sqrt(2)*t)*math.cos(15*math.cos(7*math.sqrt(2)*t))*(1/math.sqrt(2))
    #y
    v_y = 21*math.sin(7*math.sqrt(2)*t)*math.sin(15*math.cos(7*math.sqrt(2)*t))*(1/math.sqrt(2))
    
    #v total
    vel = math.sqrt((v_x)**2+(v_y)**2)
    print(v_x, v_y, vel)

def acceleration():
    pass


