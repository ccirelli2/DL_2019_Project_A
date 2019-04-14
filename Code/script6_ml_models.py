

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


# Import Dataset
dir_dataset = r'/home/ccirelli2/Desktop/GSU/2019_Spring/Deep_Learning_Spring_2019/DL_2019_Project_A/Data_files'
file_name = 'Vectorized_text_4_selected_tokens.xlsx'
df = pd.read_excel(dir_dataset + '/' + file_name)

# Separate Features / Targets
df_features = df.drop('LABEL', axis = 1)
df_target = df['LABEL']

# Random Forest Model
RF_model1 = m6.train_RandomForecast_classifier(df_features, df_target, 6, 'Classification_report')
print(RF_model1)







