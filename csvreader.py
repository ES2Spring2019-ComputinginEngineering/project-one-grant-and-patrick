import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np
import csv

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