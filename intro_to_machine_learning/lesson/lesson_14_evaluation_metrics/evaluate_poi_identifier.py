#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation
import numpy as np

data_dict = pickle.load(open("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
features_train,features_test,labels_train,labels_test = cross_validation.train_test_split(features,labels,test_size=0.3,
                                                                                          random_state=42)
clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)
clf.score(features_test,labels_test)

# How many POIs are in the test set for your POI identifier?
pred = clf.predict(features_test)
sum(pred)
print len([e for e in labels_test if e == 1.0])

# How many people total are in your test set?
len(pred)

# If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?
1.0 - 5.0/29

# Precision and recall can help illuminate your performance better. 
# Use the precision_score and recall_score available in sklearn.metrics to compute those quantities.

# What’s the precision?
from sklearn.metrics import *

precision_score(labels_test, pred)

# What’s the recall? 
recall_score(labels_test, pred)

# Here are some made-up predictions and true labels for a hypothetical test set; 
# fill in the following boxes to practice identifying true positives, false positives, true negatives, and false negatives. 
# Let’s use the convention that “1” signifies a positive result, and “0” a negative. 
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

# What's the precision of this classifier?
precision_score(true_labels, predictions)

# What's the recall of this classifier?
recall_score(true_labels, predictions)

