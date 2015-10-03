#!/usr/bin/python 

""" 
    skeleton code for k-means clustering mini-project

"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than 4 clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)    
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("C:/Vindico/Projects/Code/Python/Python/Course/Udacity/Intro to Machine Learning/ud120-projects-master/final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2,feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, line below assumes 2 features)
for f1, f2, f3 in finance_features:
    plt.scatter( f1, f2 ,f3)
plt.show()



from sklearn.cluster import KMeans
features_list = ["poi", feature_1, feature_2,feature_3]
data2 = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data2 )
clf = KMeans(n_clusters=2)
pred = clf.fit_predict( finance_features )
Draw(pred, finance_features, poi, name="clusters_before_scaling.pdf", f1_name=feature_1, f2_name=feature_2)


### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"

# Find exercised_stock_options
import operator
stock = {k: v['exercised_stock_options'] for k, v in data_dict.items() if v['exercised_stock_options'] != 'NaN'}

# Maximum exercised_stock_options
maxval = max(stock.iteritems(), key=operator.itemgetter(1))[1]
max_stock = {k: v for k,v in stock.items() if v==maxval}
max_stock

# Minimum exercised_stock_options
minval = min(stock.iteritems(), key=operator.itemgetter(1))[1]
min_stock = {k: v for k,v in stock.items() if v==minval}
min_stock

# Stocks
ex_stok = []
for users in data_dict:
    val = data_dict[users]["exercised_stock_options"]
    if val == 'NaN':
        continue
    ex_stok.append(val)
print max(ex_stok)
print min(ex_stok)

# Find salary
salary = {k: v['salary'] for k, v in data_dict.items() if v['salary'] != 'NaN'}
# Maximum salary
maxval = max(salary.iteritems(), key=operator.itemgetter(1))[1]
max_salary = {k: v for k,v in salary.items() if v==maxval}
max_salary

# Minimum salary
minval = min(salary.iteritems(), key=operator.itemgetter(1))[1]
min_salary = {k: v for k,v in salary.items() if v==minval}
min_salary

# Salary
salary = []
for users in data_dict:
    val = data_dict[users]["salary"]
    if val == 'NaN':
        continue
    salary.append(val)
    
print max(salary)
print min(salary)

#{k: v['salary'] for k, v in data_dict.items() if v['salary'] != 'NaN' and v['salary'] < 4000}



