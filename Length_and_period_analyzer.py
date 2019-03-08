#Length and period analyzer/grapher

#Created by: Grant Smith and Patrick Wright

#This script simply finds and graphs the relationship between the real-world length & period on one graph
#and simulated length & period on another in log-log format. 

import matplotlib.pyplot as plt
import numpy as np

lengthlist = np.asarray([.145,.15,.17,.212,.224,.226])
real_periodlist = np.asarray([291.1, 280, 310, 380, 380, 390])
simulated_periodlist = np.asarray([764, 778, 828, 924, 950, 954])

plt.plot(lengthlist, real_periodlist, 'r-')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('log(Period) (ms)')
plt.xlabel('log(Length) (m)')
plt.title('Real-life period vs. length (log-log scale)')
plt.show()

plt.plot(lengthlist, simulated_periodlist, 'r-')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('log(Period) (ms)')
plt.xlabel('log(Length) (m)')
plt.title('Simulated period vs length (log-log scale)')
plt.show()