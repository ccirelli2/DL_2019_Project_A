

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



def train_RandomForecast_classifier(X,Y, random_state_value, result):

    x_train, x_test, y_train, y_test = train_test_split(X, Y, 
                                                        stratify = Y)
    
    # Generate Prediction
    clf_RF = RandomForestClassifier(n_estimators = 100)
    clf_RF.fit(x_train, y_train)
    y_predict = clf_RF.predict(x_test)

    # Generate Results
    if result == 'Classification_report':
        NB_class_report = sklearn.metrics.classification_report(y_test, y_predict)
        return NB_class_report
    elif result == 'f1_score':
        NB_f1_score = sklearn.metrics.f1_score(y_test, y_predict)
        return NB_f1_score
    elif result == 'precision_score':
        NB_precision_score = sklearn.metrics.precision_score(y_test, y_predict, average = None)
        return NB_precision_score
    elif result == 'recall_score':
        NB_recall_score = sklearn.metrics.recall_score(y_test, y_predict)
        return NB_recall_score
    elif result == 'feature_importance':
        Feature_important = clf_RF.feature_importances_
        df = pd.DataFrame({}, index = X.columns)
        df['Feature Importance'] = Feature_important
        m0.write_to_excel(df, 'Feature_Importance', output_dir)
        return clf_RF.score(x_test, y_test)









