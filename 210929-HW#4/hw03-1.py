
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
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


# Calculate OLS(Ordinary Least Square) regression score
linear_regression = LinearRegression()
MSE5 = cross_val_score(linear_regression, X, y, scoring='neg_mean_squared_error', cv=5)
mean_MSE = np.mean(MSE5)
print("\nlinear_regression")
print(mean_MSE, end="\n\n")


# Calculate Ridge regression score
ridge = Ridge()
parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-3, 1e-2, 1, 5, 10, 20]}
ridge_regressor = GridSearchCV(ridge, parameters, scoring='neg_mean_squared_error', cv=5)
ridge_regressor.fit(X, y)
# find the best parameter and the best MSE
print("ridge_regressor")
print(ridge_regressor.best_params_)
print(ridge_regressor.best_score_, end="\n\n")


# Calculate Lasso regression score
lasso = Lasso(tol=0.1)
parameters = {'alpha': [1e-15, 1e-10, 1e-8, 1e-4, 1e-3, 1e-2, 1, 5, 10, 20]}
lasso_regressor = GridSearchCV(lasso, parameters, scoring='neg_mean_squared_error', cv=5)
lasso_regressor.fit(X, y)

# find the best parameter and the best MSE
print("lasso_regressor")
print(lasso_regressor.best_params_)
print(lasso_regressor.best_score_, end="\n\n")