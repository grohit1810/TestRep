# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:38:06 2019

@author: 19233292
"""

import numpy as np
#linspace

lin =np.linspace(0,2,9)
print (lin)

log_space = np.logspace(-6,0,7)
print (log_space)



norm_dist = np.random.normal(1.98,4.98,(1000000000,1))
print(norm_dist,np.mean(norm_dist),np.std(norm_dist))