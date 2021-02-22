import numpy as np
from brian2 import *

# PARAMETERS

defaultclock.dt = 0.1 * ms # for better precision

b_e = 1.3
thet_e = 4

b_i = 2.0
thet_i = 3.7

k_e = 1/(1/np.exp(b_e * thet_e)+1) # 0.9945
k_i = 1/(1/np.exp(b_i * thet_i)+1) # 0.9994

# tau values must be 10 +/- 20ms
tau_cx = 10 * ms
tau_th = 10 * ms
tau_nrt = 10 * ms
tau_dcn = 10 * ms
tau_gpe = 10 * ms
tau_gpi = 10 * ms
tau_stn = 10 * ms

ext = 3.42

# WEIGHTS

W ={}

## Healthy state parameters
W['healthy'] = [20, 5, 8, 25, 15, 5, 19, 5, 15, 20, 20]


## Tremor band parameters
W['tremor'] =[20, 12, 8, 9, 15, 5, 5, 5, 15, 20, 20]


## Beta band parameters
W['beta'] = [0, 20, 5, 8, 20, 15, 5, 5, 5, 15, 20, 20]

# DBS

A = 5
f = 120