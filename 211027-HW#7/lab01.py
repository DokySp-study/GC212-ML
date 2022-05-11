
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np


# Print each encoded features.
def print_label(arr):
    print("aspiration: ", end="")
    print(aspiration_label[arr[0]])
    print("doornumber: ", end="")
    print(doornumber_label[arr[1]])
    print("drivewheel: ", end="")
    print(drivewheel_label[arr[2]])
    print("cylindernumber: ", end="")
    print(cylindernumber_label[arr[3]])
    print("fueltype: ", end="")
    print(fueltype_label[arr[4]])


# Read csv file
df = pd.read_csv("data.csv")


# Create labelEncoder
le = preprocessing.LabelEncoder()

# Convert string labels into numbers.
aspiration_encoded=le.fit_transform(df["aspiration"])
aspiration_label = le.classes_
# print(le.classes_)

doornumber_encoded=le.fit_transform(df["doornumber"])
doornumber_label = le.classes_
# print(le.classes_)

drivewheel_encoded=le.fit_transform(df["drivewheel"])
drivewheel_label = le.classes_
# print(le.classes_)

cylindernumber_encoded=le.fit_transform(df["cylindernumber"])
cylindernumber_label = le.classes_
# print(le.classes_)

fueltype_encoded=le.fit_transform(df["fueltype"])
fueltype_label = le.classes_
# print(le.classes_)

# target feature
# range: 5118 ~ 45400 -> 3 bins
label = np.digitize( df['price'], bins=np.linspace(5118, 45400, 4) )
target_label = np.linspace(5118, 45400, 4)
# print(target_label)


# Build dataframe
X = pd.DataFrame({
    "aspiration": aspiration_encoded,
    "doornumber": doornumber_encoded,
    "drivewheel": drivewheel_encoded,
    "cylindernumber": cylindernumber_encoded,
    "fueltype": fueltype_encoded,
})

# Use Naive Bayesian model
model = GaussianNB()
model.fit(X, label)


# Predict and print result
def predict_option(arr):
    print_label(arr)
    predicted= model.predict( [arr] )
    
    print("Predicted price range: $", end="")
    print(int(target_label[predicted-1][0] * 100) / 100, end="")
    print(" ~ $", end="")
    print(int(target_label[predicted][0] * 100) / 100)
    

# Predict various options
print("")
target = [0,0,1,2,1]
predict_option(target)
print("")

target = [0,0,1,2,0]
predict_option(target)
print("")

print("")
target = [0,1,2,2,1]
predict_option(target)
print("")

target = [1,1,2,0,1]
predict_option(target)
print("")

# Print model score
print("Model score: ", end="")
print(model.score(X, label))
