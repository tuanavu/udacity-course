#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/final_project/final_project_dataset.pkl", "r") )

data_dict['TOTAL']
data_dict.pop('TOTAL',0)
#[s for s in data_dict.keys() if "TOTAL" in s]
#data_dict['TOTAL']

features = ["salary", "bonus"]

data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

import numpy
numpy.amax(data)

# Check for Outliers
#{k: v for k, v in data_dict.items() if v['bonus'] != 'NaN' and v['bonus'] > 4000000}

from pprint import pprint

outliers = []
for key in data_dict:
    val = data_dict[key]['salary']
    if val == 'NaN':
        continue
    outliers.append((key,int(val)))

pprint(sorted(outliers,key=lambda x:x[1],reverse=True)[:2])