# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 18:17:51 2014

@author: tvu
"""

def classify(features_train, labels_train):
    
    ### your code goes here--should return a trained decision tree classifer
    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features_train, labels_train)   
    return clf