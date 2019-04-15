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
from sklearn.model_selection import RandomizedSearchCV


def train_RandomForecast_classifier(X,Y, result, target):
    
    # Create Train / Test Split for Features & Target
    x_train, x_test, y_train, y_test = train_test_split(X, Y, stratify = Y)
    
    # Instantiate the RF Model 
    clf_RF = RandomForestClassifier(n_estimators      = 2000, 
                                    min_samples_split = 2, 
                                    min_samples_leaf  = 2, 
                                    max_features      = 'auto', 
                                    max_depth         = 50, 
                                    bootstrap         = False)

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


def train_KneighborsClassifier(X, Y, num_neighbors, target):
    
    # Create Train / Test Split for Features & Target
    x_train, x_test, y_train, y_test = train_test_split(X, Y, stratify = Y)
    
    clf_KNN = KNeighborsClassifier(n_neighbors = num_neighbors)
    clf_KNN.fit(x_train, y_train)
    y_predict = clf_KNN.predict(x_test)


    if target == 'train':
        return accuracy_score(y_train, clf_KNN.predict(x_train))

    elif target == 'test':
        return accuracy_score(y_test, y_predict)

    # Return
    return None






##########    Try RandomizedSearchCV     ####################


















