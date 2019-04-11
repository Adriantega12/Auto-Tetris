'''
Machine learning algorithm will be done in here
'''

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC

data_frame = pd.read_csv('Data.csv')

x = np.asanyarray(data_frame.drop(columns = ['Output']))
y = np.asanyarray(data_frame.Output)

x_train, x_test, y_train, y_test = train_test_split(x, y)

print(data_frame.info())

# MLP
mlp_model = MLPClassifier()
mlp_model.fit(x_train, y_train)
y_pred_mlp = mlp_model.predict(x_test)

print('Classification report:')
print(metrics.classification_report(y_test, y_pred_mlp))
print('Confusion matrix:')
print(metrics.confusion_matrix(y_test, y_pred_mlp))
print('MLP Score: ')
print('- Test: ', mlp_model.score(x_test, y_test))

# SVC
svc_model = SVC()
svc_model.fit(x_train, y_train)
y_pred_svc = mlp_model.predict(x_test)

print('Classification report:')
print(metrics.classification_report(y_test, y_pred_svc))
print('Confusion matrix:')
print(metrics.confusion_matrix(y_test, y_pred_svc))
print('SVC Score: ')
print('- Test: ', svc_model.score(x_test, y_test))
