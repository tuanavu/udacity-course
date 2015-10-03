# -*- coding: utf-8 -*-
"""
Created on Sat Dec 06 14:11:46 2014

@author: tvu
"""

from sklearn.preprocessing import MinMaxScaler
import numpy
weights = numpy.array([[115.], [140.], [175.]])
scaler = MinMaxScaler()
rescaled_weight = scaler.fit_transform(weights)
rescaled_weight


    