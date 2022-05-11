
import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

# Dataset from Kaggle
# https://www.kaggle.com/mirichoi0218/insurance
df = pd.read_csv('./insurance.csv')

# Drop not correlated features
df = df[df['smoker'] == 'no']
df = df.drop(['sex', 'region', 'smoker'], axis=1)

# Seperate feature and target data.
X = df.iloc[:,0:3]
y = df.iloc[:,3]

# Target variables are too big, so this need to be scaled
scaler = StandardScaler()
y = scaler.fit_transform(y.values.reshape(-1,1))


# Calculate ElasticNet regression score
elasticNet = ElasticNet()
parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-3, 1e-2, 1, 5, 10, 20]}
elasticNet_regressor = GridSearchCV(elasticNet, parameters, scoring='neg_mean_squared_error', cv=5)
elasticNet_regressor.fit(X, y)

# find the best parameter and the best MSE
print("\nelasticNet_regressor")
print(elasticNet_regressor.best_params_)
print(elasticNet_regressor.best_score_)