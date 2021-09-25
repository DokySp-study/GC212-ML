
import numpy as np
import pandas as pd


df = pd.read_csv("./data.csv")

# print(df.info())
print("======================")
print(df.describe())
print("======================")
# print(df.isna().sum())





















# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeRegressor
# from sklearn import preprocessing
# from sklearn.model_selection import GridSearchCV

# from IPython.display import Image
# from sklearn.tree import export_graphviz  


# # Make dataframe
# df = pd.DataFrame({
#     "Major" : ["SW", "Math", "Art", "English", "Math", "English", "Math", "SW", "SW", "English", "Math", "Math", "SW", "Art"],
#     "Year" : [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
#     "Gender" : ["F", "M", "F", "M", "F", "M", "F", "F", "M", "M", "M", "F", "F", "M"],
#     "StudyHours" : [20, 20, 15, 28, 26, 17, 26, 40, 33, 18, 25, 30, 45, 20],
# })


# # Preprocessing (String to categorical data)
# labelEncoder = preprocessing.LabelEncoder()

# majorClasses = labelEncoder.fit(df.iloc[:,0]).classes_
# genderClasses = labelEncoder.fit(df.iloc[:,2]).classes_
# result = labelEncoder.fit_transform(df.iloc[:,0])
# df["Major"] = result
# result = labelEncoder.fit_transform(df.iloc[:,2])
# df["Gender"] = result


# # Split train and test set (Manipulated)
# X = df.iloc[:, 0:3]
# y = df.iloc[:, 3]
# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=12, shuffle=True)


# # Make Decision tree regression model and fit
# model = DecisionTreeRegressor()
# model.fit(x_train, y_train)


# # Scoring model
# score = model.score(x_test, y_test)
# print(score)


# # Represent result tree image
# print("Categorical Data's index")
# print(pd.DataFrame({"Major": majorClasses}))
# print(pd.DataFrame({"Gender": genderClasses}))

# # Export Decision Tree with PlantUML
# export_graphviz(model, out_file ='tree.dot') 
# with open("tree.dot") as f:
#     dot_graph = f.read()
# print("\nCopy and paste code to http://www.plantuml.com/plantuml/uml/")
# print("________________________")
# print("@startuml")
# print(dot_graph)
# print("@enduml")
