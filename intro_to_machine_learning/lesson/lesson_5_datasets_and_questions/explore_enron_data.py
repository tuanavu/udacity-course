#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/final_project/final_project_dataset.pkl", "r"))

# How many data points (people) are in the dataset?
len(enron_data)
len(enron_data.keys())

# For each person, how many features are available?
len(enron_data.values()[0])
enron_data[enron_data.keys()[0]]
len(enron_data['SKILLING JEFFREY K'])

# How many POIs are there in the E+F dataset
# Example 1:
count = 0
for i in range(len(enron_data)):
    a = enron_data.values()
    if a[i]['poi'] == True:
        count = count + 1        
print count

# Example 2:
count = 0
for user in enron_data:
    if enron_data[user]['poi'] == True:
        count+=1
print count

# How Many POIs Exist?
poi_text = 'C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/final_project/poi_names.txt'
poi_names = open(poi_text, 'r')
fr = poi_names.readlines()
len(fr[2:])
poi_names.close()

# print poi_names.read()

num_lines = sum(1 for line in open(poi_text))

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

file_len('C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/final_project/poi_names.txt')

# Check if values exist in any string in the list
matching = [s for s in enron_data.keys() if "PRENTICE" in s]
matching

# What is the total value of the stock belonging to James Prentice?
enron_data['PRENTICE JAMES']['total_stock_value']

# How many email messages do we have from Wesley Colwell to persons of interest?
[s for s in enron_data.keys() if "COLWELL" in s]
enron_data['COLWELL WESLEY']
enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# What’s the value of stock options exercised by Jeffrey Skilling?
[s for s in enron_data.keys() if "SKILLING" in s]
enron_data['SKILLING JEFFREY K']['exercised_stock_options']

enron_data[enron_data.keys()[1]]

# Sort values
sorted(enron_data.keys())

# How much money did that person get?
enron_data['SKILLING JEFFREY K']['total_payments']
enron_data['FASTOW ANDREW S']['total_payments']
enron_data['LAY KENNETH L']['total_payments']

# How is an unfilled feature denoted?
enron_data['FASTOW ANDREW S']['deferral_payments']

# How many folks in this dataset have a quantified salary?
# What about a known email address?
count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary+=1
    if enron_data[key]['email_address'] != 'NaN':
        count_email+=1
print count_salary
print count_email


# How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments?
# What percentage of people in the dataset as a whole is this?
count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count_NaN_tp+=1
print count_NaN_tp
print float(count_NaN_tp)/len(enron_data.keys())
        
# How many POIs in the E+F dataset have “NaN” for their total payments? 
# What percentage of POI’s as a whole is this?   
count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
        print 
        count_NaN_tp+=1
print count_NaN_tp
print float(count_NaN_tp)/len(enron_data.keys())

    