#Data Analysis

#Created by: Grant Smith and Patrick Wright

#This will calculate the period after parsing the data and filtering it.
#Variables that should be updated depedning on the test are:
#'file' this is the path of the file that should be run in the analysis program
#'Length' this is the length of the pendulum used and is only used in nameing the graph
#'testnumber' this is the number of the test used in naming the graph
#'realorsim' this is if the test is real world data or simulation data and is used in naming the graphs


import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np
import csv 
import statistics

#global variables

file = '/Users/User/Documents/S2019/ES 2/Github/project-one-grant-and-patrick/data/simulation/testdata6L=0.212.csv' #path of file
Length = '0.212m'  #length of pendulum arm
testnumber = '6'   #number of test being performed
realorsim = 'Simulation' #if the tested file is simulation or real world data

#main script

timelist = []
acclist = []
with open(file, newline='') as csvfile:  
    read = csv.reader(csvfile)
    for row in read:
        timelist.append(row[0])
        acclist.append(row[1])
    timelist[0] = 0
for a in range(0,len(timelist)):
    timelist[a] = float(timelist[a])
for a in range(0, len(acclist)):
    acclist[a] = float(acclist[a])
timearray = np.asarray(timelist)
accarray = np.asarray(acclist)


# Apply median filter to both original and noisy wave
accfilt = sig.medfilt(accarray)

# Find peaks of all waves
acc_peaks, _ = sig.find_peaks(accfilt)


# Plot waveforms and their peaks
plt.plot(timearray, accarray, 'r-', timearray[acc_peaks], accarray[acc_peaks], 'b.')
plt.title(realorsim + ' Pendulum Length: ' + Length + ' (Test ' + testnumber + ')')
plt.ylabel('Acceleration (milli-g)')
plt.xlabel('Time (ms)')
plt.show()

# Period analysis below:
timepeaklist = (timearray[acc_peaks].tolist())
timepeakdifflist = []
for num in range(0,len(timepeaklist)-1):
    timepeakdifflist.append(timepeaklist[num+1]-timepeaklist[num])
print('List of periods before filtering: ', timepeakdifflist)
period_std_dev = np.std(timepeakdifflist)
print('Standard dev. of period (will use for filtering): ', period_std_dev) 
medianperiod = statistics.median(timepeakdifflist)
print('Median period (will be used for filtering): ', medianperiod) 
highboundary = medianperiod + period_std_dev
lowboundary = medianperiod - period_std_dev

a = 0 # Counter variable for while loop
while a < len(timepeakdifflist):
    if timepeakdifflist[a] > highboundary or timepeakdifflist[a] < lowboundary:
        print('Outliers detected -- removing ', timepeakdifflist[a])
        timepeakdifflist.pop(a) #Don't change a because list is being reindexed by removal of number!!!
    else:
        a+= 1
    
print(timepeakdifflist) #Debug
newmeanperiod = sum(timepeakdifflist)/len(timepeakdifflist)
print('Final period (numerical average): ', newmeanperiod*2, ' ms') # Note: The *2 is because the above code only finds the
# differences in time between the peak acceleration values for the pendulum. The pendulum will hit this peak acceleration
# /2 times/ per period so the period must be calculated by multiplying the difference in peak accel's by 2.