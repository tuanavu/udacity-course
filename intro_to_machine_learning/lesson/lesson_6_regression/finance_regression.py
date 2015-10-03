#!/usr/bin/python

"""
    starter code for the regression mini-project
    
    loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project)

    draws a little scatterplot of the training/testing data

    you fill in the regression code where indicated

"""    


import sys
import pickle
import os
#sys.path.append("../tools/")
os.chdir("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
# features_list = ["bonus", "long_term_incentive"]

data = featureFormat( dictionary, features_list, remove_any_zeroes=True)#, "long_term_incentive"], remove_any_zeroes=True )
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### your regression goes here!
### please name it reg, so that the plotting code below picks it up and 
### plots it correctly
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(feature_train,target_train)


print 'Coefficient: ', reg.coef_[0]

print 'Intercept: ', reg.intercept_

print '##### Stats on Training dataset ####'
print 'r-squared score: ', reg.score(feature_train,target_train)

print '##### Stats on Test dataset ####'
print 'r-squared score: ', reg.score(feature_test,target_test)





### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass
reg.fit(feature_test, target_test)
print reg.coef_[0]
plt.plot(feature_train, reg.predict(feature_train), color="r") 
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
