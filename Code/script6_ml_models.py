## Import Packages
import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
import numpy as np



# Import Modules
import module6_ml_models as m6
import module0_utility_functions as m0

# Import Dataset
dir_dataset = r'/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/DL_2019_Project_A/Data_files'
file_name = 'Second_file.xlsx'
df = pd.read_excel(dir_dataset + '/' + file_name)

# Define Output Dir
output_dir = '/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/DL_2019_Project_A/output'

# Separate Features / Targets
df_features = df.drop('LABEL', axis = 1)
df_target = df['LABEL']

# List Values Over Which To Iterate
list_values = [2,4,6,8,10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]


###########   Random Forest  #######

# Single Selector 
'''
{'n_estimators': 2000, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 'auto', 'max_depth': 50, 'bootstrap': False}

Test Accuracy:  .64
'''

def m1_rf(features, targets):
    m1_rf = m6.train_RandomForecast_classifier(df_features, df_target, 
                                           result = 'accuracy', 
                                           target = 'test')
    print(m1_rf)



# Iterate Over list Of Values To Tune Parameters
'''
for value in list_values:
    m1_rf = m6.train_RandomForecast_classifier(df_features, df_target, 
                                           random_state_value = 6, 
                                           depth = value, 
                                           leaf_nodes = value, 
                                           result = 'accuracy', 
                                           target = 'test')
    
    print('Accuracy = {} w/ depth {} and leaf_nodes = {}'.format(round(m1_rf, 2), value, value))


## Test Results
Accuracy = 0.31 w/ depth 2 and leaf_nodes = 2
Accuracy = 0.38 w/ depth 4 and leaf_nodes = 4
Accuracy = 0.42 w/ depth 6 and leaf_nodes = 6
Accuracy = 0.48 w/ depth 8 and leaf_nodes = 8
Accuracy = 0.5 w/ depth 10 and leaf_nodes = 10
Accuracy = 0.51 w/ depth 12 and leaf_nodes = 12
Accuracy = 0.49 w/ depth 14 and leaf_nodes = 14
Accuracy = 0.44 w/ depth 16 and leaf_nodes = 16
Accuracy = 0.52 w/ depth 18 and leaf_nodes = 18
Accuracy = 0.53 w/ depth 20 and leaf_nodes = 20
Accuracy = 0.51 w/ depth 22 and leaf_nodes = 22
Accuracy = 0.52 w/ depth 24 and leaf_nodes = 24
Accuracy = 0.5 w/ depth 26 and leaf_nodes = 26
Accuracy = 0.54 w/ depth 28 and leaf_nodes = 28
Accuracy = 0.51 w/ depth 30 and leaf_nodes = 30
'''



###########    KNN    ##########

'''
for n in list_values:
    m1_KNN = m6.train_KneighborsClassifier(df_features, df_target, n, 'test')
    print('Accuracy score => {} using {} number of nearest neighbors'.format(round(m1_KNN,2), n))

# Test Results
Accuracy score => 0.39 using 2 number of nearest neighbors
Accuracy score => 0.46 using 4 number of nearest neighbors
Accuracy score => 0.47 using 6 number of nearest neighbors
Accuracy score => 0.49 using 8 number of nearest neighbors
Accuracy score => 0.48 using 10 number of nearest neighbors
Accuracy score => 0.41 using 12 number of nearest neighbors
Accuracy score => 0.49 using 14 number of nearest neighbors
Accuracy score => 0.46 using 16 number of nearest neighbors
Accuracy score => 0.42 using 18 number of nearest neighbors
Accuracy score => 0.48 using 20 number of nearest neighbors
Accuracy score => 0.47 using 22 number of nearest neighbors
Accuracy score => 0.46 using 24 number of nearest neighbors
Accuracy score => 0.48 using 26 number of nearest neighbors
Accuracy score => 0.44 using 28 number of nearest neighbors
Accuracy score => 0.45 using 30 number of nearest neighbors

'''




####### TRY RANDOM HYPERPARAMETER GRID    ################
'''
# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}


# Instantiate 
rf = RandomForestClassifier()
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, 
                                n_iter = 10, cv = 3, verbose = 2, random_state = 42, 
                                n_jobs = -1)



# Fit Model
rf_random.fit(df_features, df_target)



print('@@@@@@@@@', rf_random.best_params_)
'''





























