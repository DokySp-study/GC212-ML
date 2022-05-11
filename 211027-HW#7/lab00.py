


from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import pandas as pd



df = pd.DataFrame({
        "weather": ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast',' Sunny','Sunny', 'Rainy','Sunny','Overcast','Overcast','Rainy'],
        "temp": ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild', 'Mild','Hot','Mild'],
        "play": ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes' ,'No'],
    }
)

# aspiration
# doornumber 2
# drivewheel 11
# wheelbase continuous -> binning 86.6 ~ 121 (5 bins)
# fuel type 2

# car price -> binning 5118 ~ 45400 (10 bins)


dft = pd.read_csv("data.csv")

print(dft['cylindernumber'].drop_duplicates().to_numpy())
print("")


#create labelEncoder
le = preprocessing.LabelEncoder()
# Convert string labels into numbers.
weather_encoded=le.fit_transform(df["weather"])
print(le.classes_)
temp_encoded=le.fit_transform(df["temp"])
print(le.classes_)
label=le.fit_transform(df["play"])
print(le.classes_)



X = pd.DataFrame({
    "weather": weather_encoded,
    "temp": temp_encoded,
})

print(X)



model = GaussianNB()
model.fit(X, label)

predicted= model.predict([[1,2]]) # 1:Overcast, 2:Mild print "Predicted Value:", predicted
print(predicted)
print(model.score(X, label))