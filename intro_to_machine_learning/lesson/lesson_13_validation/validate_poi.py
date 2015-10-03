#!/usr/bin/python


"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!

    start by loading/formatting the data

    after that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn import cross_validation

data_dict = pickle.load(open("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  
clf = DecisionTreeClassifier()
clf.fit(features, labels)
clf.score(features,labels)
# 0.98958333333333337

# Now you’ll add in training and testing, so that you get a trustworthy accuracy number. 
# Use the training_test_split validation available in sklearn.cross_validation

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features,
                labels,test_size=0.3,random_state=42)
                
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
clf.score(features_test,labels_test)
# 0.72413793103448276

