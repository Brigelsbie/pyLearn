# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 15:34:29 2025

@author: Brigelsbie
"""

#%% import libraries
# plt is standard for plot

import numpy as np
import matplotlib.pyplot as plt

#%% read the data
 data = np.loadtxt(fname = 'inflammation-01.csv', 
                   delimiter = ',')
 
 
 #%% plot the entire dataset
 
 image = plt.imshow(data)
 
 # this next line may be optional depending on python environment
 # default is most recent plot
 # plt.show()
 
 #%% subset, aggregate, visualize
 
 ave_inflammation = np.mean(data, axis = 0)
 ave_plot = plt.plot(ave_inflammation)
 
 #%% max value plot
 
max_plot = plt.plot(np.amax(data, axis = 0))

#%% min value plot

min_plot = plt.plot(np.amin(data, axis = 0))

#%% grouping plots in figures
# figure is a container for multiple plots
# figsize essentially size in inches
fig = plt.figure(figsize = (10.0, 3.0))

# define subplots
# 3 parameters, subplot container

# 1 plot high, 3 plots wide, 1st position
axes1 = fig.add_subplot(1, 3, 1)

# 1 plot high, 3 plots wide, 2nd position
axes2 = fig.add_subplot(1, 3, 2)

# 1 plot high, 3 plots wide, 3rd position
axes3 = fig.add_subplot(1, 3, 3)

# plot data
axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis = 0))

axes2.set_ylabel('max')
axes2.plot(np.amax(data, axis = 0))
 
axes3.set_ylabel('min')
axes3.plot(np.amin(data, axis = 0))

# manage whitespace in plots
fig.tight_layout()

# save 
plt.savefig('inflammation.png')

 
 
 
 
 
 


