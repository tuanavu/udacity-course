#!/usr/bin/python

import pickle
import numpy
from time import time
numpy.random.seed(42)


### the words (features) and authors (labels), already largely processed
path = "C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/text_learning/"
words_file = path + "your_word_data.pkl" ### like the file you made in the last mini-project 
authors_file = path + "your_email_authors.pkl"  ### this too
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (remainder go into training)
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train).toarray()
features_test  = vectorizer.transform(features_test).toarray()

### a classic way to overfit is to use a small number
### of data points and a large number of features
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150]
labels_train   = labels_train[:150]



### your code goes here
from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t0, 3), "s"
acc = accuracy_score(pred, labels_test)
print acc 

# How many training points are there, according to the starter code?
len(features_train)


# What’s the importance of the most important feature? What is the number of this feature?
importances = clf.feature_importances_
for index, item in enumerate(importances):
    if item > 0.2:        
        print index, item       
       
import numpy as np
indices = np.argsort(importances)[::-1]
print 'Feature Ranking: '
for i in range(10):
    print "{} feature no.{} ({})".format(i+1,indices[i],importances[indices[i]])

# What’s the most powerful word when your decision tree is makeing its classification decisions?
feature_name = vectorizer.get_feature_names()
for index, item in enumerate(feature_name):
    if index == 33614:        
        print item

vectorizer.get_feature_names()[33614]
# Result: sshacklensf      
        
feature_name = vectorizer.get_feature_names()
for index, item in enumerate(feature_name):
    if index == 14343:        
        print item 
        
vectorizer.get_feature_names()[14343]
# Result: cgermannsf
        
feature_name = vectorizer.get_feature_names()
for index, item in enumerate(feature_name):
    if index == 14343:        
        print item 
# Result: houectect


