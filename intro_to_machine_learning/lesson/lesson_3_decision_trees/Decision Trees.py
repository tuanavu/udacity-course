# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 18:33:02 2014

@author: tvu
"""

import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################


########################## DECISION TREE #################################
from sklearn import tree
from sklearn.metrics import accuracy_score

#### your code goes here

clf = tree.DecisionTreeClassifier(min_samples_split=50)
clf.fit(features_train, labels_train)   
pred = clf.predict(features_test)

acc = accuracy_score(pred, labels_test)
### be sure to compute the accuracy on the test set
print acc

    
#def submitAccuracies():
#  return {"acc":round(acc,3)}

