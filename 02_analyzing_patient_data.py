# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 14:39:47 2025

@author: Brigelsbie
"""

#%% import libraries
# using np alias

import numpy as np

#%%read data from file
#2 arguements needed
#fname = filename string
#delimiter = how data is organized (comma, tab, etc)

print (np.loadtxt(fname='inflammation-01.csv',
          delimiter=',' ))

#%% save data to a variable

data = np.loadtxt(fname='inflammation-01.csv', 
                  delimiter=',')

# see the data for sanity check
print(data)

#%% inspect the data

# attributes do not have arguements

print(type(data)) # the data type of the data object

print(data.dtype) # data type of the array values

print(data.shape) # nrows, ncols

#%% accessing values in an array
# [row_selecter, column_selecter]

print('first value in data:', data[0, 0] )

#%% python uses zero indexing
# zero offset
# [0, 1, 2, 3] = first, second, third, fourth element in list

# middle value in the data
print('middle value in data:', data[29, 19])

#%% slice data
# [start_row_pos:end_row_pos, start_col_pos:end_col_pos]
# end pos is up to but not including

# the first 4 rows and first 10 columns
print(data[0:4, 0:10])

# can specify any start point position
print(data[5:10, 0:10])

# don't need to specify start or end if that range is fine
print(data[:3, 36:])

#%% analyzing the data
# average (avg) value in the dataset
# may test for null values

print(np.mean(data))

#%% assign multiple variables at once (sucks for readabilty)

maxval, minval, stdval = np.amax(data), np.amin(data), np.std(data)

print('max inflammation:', maxval)
print('min inflammation:', minval)
print('standard deviation:', stdval)

# rounding function, specify decimal percentage
print('standard deviation:', round(stdval, 3))

#%% subset and aggregate
# the verbose approach

patient_0 = data[0,:]
print('max inflammation for patient zero:', 
      np.amax(patient_0))

#%% less verbose, more concise
# max inflammation for patient two

print('max inflammation value for patient two:',
      np.amax(data[2, :]))

# max inflammation for patient one
print('max inflammation value for patient one:',
      np.amax(data[1, :]))

# aggragating column vs row can be confusing

#%% average inflammation for all days

print(np.mean(data, axis = 0))

#%% sanity check
# shows the number of columns used

print(np.mean(data, axis = 0).shape)

#%% average inflamation per patient 

print(np.mean(data, axis = 1))



















































