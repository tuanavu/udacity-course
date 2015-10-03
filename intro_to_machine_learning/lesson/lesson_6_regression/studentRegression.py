# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 22:04:30 2014

@author: tvu
"""

def studentReg(ages_train, net_worths_train):
    ### import the sklearn regression module, create, and train your regression
    ### name your regression reg
    
    ### your code goes here!
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(ages_train, net_worths_train)
    
    return reg