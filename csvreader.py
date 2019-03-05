import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np
import csv 
import statistics

timelist = []
acclist = []
with open('FINALdata.csv', newline='') as csvfile:
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
plt.title('Original')
plt.show()

# Period analysis below:
timepeaklist = (timearray[acc_peaks].tolist())[4:11]
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
print('Final period (numerical average): ', newmeanperiod, ' ms')