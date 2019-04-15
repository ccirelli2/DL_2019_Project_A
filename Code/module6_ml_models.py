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
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt



def train_RandomForecast_classifier(X,Y, random_state_value, 
                                    depth, leaf_nodes, result,
                                    target):
    
    # Create Train / Test Split for Features & Target
    x_train, x_test, y_train, y_test = train_test_split(X, Y, stratify = Y)
    
    # Instantiate the RF Model 
    clf_RF = RandomForestClassifier(n_estimators = 200, 
                                   max_depth = depth, 
                                   max_leaf_nodes = leaf_nodes,  
                                   max_features = 'auto')

    # Train the Model 
    clf_RF.fit(x_train, y_train)
    # Generate & Prediction On X_test data
    y_predict = clf_RF.predict(x_test)
    
    if result == 'accuracy':

        if target == 'train':
            return accuracy_score(y_train, clf_RF.predict(x_train))
        
        elif target == 'test':
            return accuracy_score(y_test, y_predict)

    # Return
    return None



















