# -*- coding: utf-8 -*-
"""
Created on Mon Aug 05 04:12:52 2019

@author: catas
"""

import numpy as np
import math
import matplotlib.pyplot as plt
print 
X = np.arange(-30,-20, dtype=np.float)
Y1 = []
Y2 = []

for x in X: #Para valores practicos 
    
    y = 1.
    t = 1.
    k = 1.

    while y != y+t*x/k:
        t = t*x/k
        y = y+t
        k = k+1
    Y1.append(y)

for x in X: #Para valores a partir de math
    
    Y2.append(math.exp(x))
    
plt.figure(num=None, figsize=(10, 3), dpi=80, facecolor='w', edgecolor='k')

plt.plot(X, Y1, "r")
plt.plot(X, Y2, "b")


plt.title('exp()')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

print Y1
print Y2