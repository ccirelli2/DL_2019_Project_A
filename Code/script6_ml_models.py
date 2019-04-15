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


### Random Forest

# Single Selector 
'''
m1_rf = m6.train_RandomForecast_classifier(df_features, df_target, 
                                           random_state_value = 6, 
                                           depth = 22, 
                                           leaf_nodes = 22, 
                                           result = 'accuracy', 
                                           target = 'train')

'''


# Iterate Over list Of Values To Tune Parameters
'''
for value in list_values:
    m1_rf = m6.train_RandomForecast_classifier(df_features, df_target, 
                                           random_state_value = 6, 
                                           depth = value, 
                                           leaf_nodes = value, 
                                           result = 'accuracy', 
                                           target = 'test')
    print(value, m1_rf)
'''



























