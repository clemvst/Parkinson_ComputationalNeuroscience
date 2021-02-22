import numpy as np

# PARAMETERS

i = 'i'
e = 'e'

b = {e: 1.3, i: 2.0}
thet = {e: 4.0, i: 3.7}
k = {e: 1/(1/np.exp(b[e]*thet[e])+1), i: 1/(1/np.exp(b[i]*thet[i])+1)}

ext=3.42
tau=0.010 # we take the same for all calculations


# WEIGHTS

W ={}

## Healthy state parameters
W['healthy'] = [0, 20, 5, 8, 25, 15, 5, 19, 5, 15, 20, 20] # start at 0 to have a w0 value (unused)

## Tremor band parameters
W['tremor'] =[0, 20, 12, 8, 9, 15, 5, 5, 5, 15, 20, 20] # start at 0 to have a w0 value (unused)


## Beta band parameters
W['beta'] = [0, 20, 5, 8, 20, 15, 5, 5, 5, 15, 20, 20] # start at 0 to have a w0 value (unused)

# DBS

A = 5
f = 120