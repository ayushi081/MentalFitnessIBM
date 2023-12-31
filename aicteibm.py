# -*- coding: utf-8 -*-
"""AICTEIBM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nxYoS48HZ_DT1M3BzVDElB06KlTMZaSS
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the datasets
df_dalys = pd.read_csv('daly.csv')
df_prevalence = pd.read_csv('pd.csv')

df_merged = pd.merge(df_dalys, df_prevalence, on=['Entity', 'Code', 'Year'])

# Feature Engineering
# Select relevant features for mental fitness tracking
features = [ 'Schizophrenia','Bipolar disorder','Eating disorders',' Anxiety disorders','Drug use disorders','Depressive disorders','Alcohol use disorders']

#set axis
df_merged.set_axis(['Country','Code','Year','DALY','Schizophrenia','Bipolar disorder','Eating disorders',' Anxiety disorders','Drug use disorders','Depressive disorders','Alcohol use disorders'], axis='columns', inplace='True')

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(12,6))
sns.heatmap(df_merged.corr(),annot=True,cmap='Blues')
plt.plot()

sns.pairplot(df_merged,corner=True)
plt.show()

mean=df_merged['DALY'].mean()
mean

import plotly.express as px
fig=px.pie(df_merged,values='DALY',names='Year')
fig.show()

# Split the dataset into features (X) and target variable (y)
X = df_merged[features]
y = df_merged['DALY']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score

# Model Training Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)
Score= r2_score(y_test,y_pred)
print('r2 Score of Model:', Score)

# Real-Time Tracking (Example: Predict mental fitness label for a new data point)
new_data = pd.DataFrame([[ 0.1, 0.2, 0.3, 0.4, 0.5,0.1,0.2]], columns=features)
prediction = model.predict(new_data)
print('Predicted Mental Fitness Label:', prediction)

#yearwise variation in Different countries mental fitness
fig=px.line(df_merged,x='Year',y='DALY',color='Country' ,markers=True,template='plotly_dark')
fig.show()