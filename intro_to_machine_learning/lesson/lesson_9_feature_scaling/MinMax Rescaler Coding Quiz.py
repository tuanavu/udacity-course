# -*- coding: utf-8 -*-
"""
Created on Sat Dec 06 14:51:27 2014

@author: tvu
"""

""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might 
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!  
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):
    # Example 1:
#    a = []
#    for i in range(len(arr)):
#        if min(arr) != max(arr):
#            x = (float(arr[i]) - min(arr))/(max(arr) - min(arr))
#            a.append(x)
#            
#        else:
#            print 'error'
#            break
#    return a
    
    # Example 2:
    nmax = max(data)
    nmin = min(data)
    if (nmax == nmin):
        return None
    normalize = nmax - nmin
    return [float(e-nmin)/normalize for e in data ]
    

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)