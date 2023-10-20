import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics

import warnings
warnings.filterwarnings('ignore')

Predict = pd.read_csv('Reliance.csv')
Predict1=Predict.iloc[0:20,:]
print(Predict1)

Predict2=Predict1.describe()
print(Predict2)

Predict3=Predict.info()
print=(Predict3)


plt.figure(figsize=(15,5))
plt.plot (Predict1['Close'])
plt.title(' Reliance Close price', fontsize=20)
plt.ylabel('Price in dollars.')
plt.show()


features = ['Open', 'High', 'Low', 'Close', 'Volume']
plt.subplots(figsize=(20,10))
for a, b in enumerate(features):
   plt.subplot(2,3,a+1)
   sb.distplot(Predict1[b])
plt.show()



features = Predict1[['open-close', 'low-high']]
target = Predict1['target']

scaler = StandardScaler()
features = scaler.fit_transform(features)

X_train, X_valid, Y_train, Y_valid = train_test_split(
	features, target, test_size=0.1, random_state=2022)
print(X_train.shape, X_valid.shape)

























