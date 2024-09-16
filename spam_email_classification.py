# -*- coding: utf-8 -*-
"""Spam Email Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S9qwtP4MAR4wbBpTpdAtXW7Prpzmn_8x
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

df = pd.read_csv('/content/emails.csv')
df.head(10)

df.shape

df.isna().sum()

df.info()

df.dtypes

# dropping email no because it is irrelevant
df = df.drop(['Email No.'],axis = 1)
df.head()

X = df.iloc[: ,:-1]
Y = df.iloc[: ,-1]

scaler = MinMaxScaler()
X= scaler.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

# Linear kernel(best model)
model = SVC(kernel='linear')
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)
print('Accuracy:',acc)
# Accuracy: 0.970048309178744

# rbf kernel
model = SVC(kernel='rbf')
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)
print('Accuracy:',acc)
# Accuracy: 0.9632850241545894

# poly  kernel
model = SVC(kernel='poly')
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)
print('Accuracy:',acc)
# Accuracy: 0.7603864734299517

# sigmoid  kernel
model = SVC(kernel='sigmoid')
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test,y_pred)
print('Accuracy:',acc)
# Accuracy: 0.8628019323671497