import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing the dataset
importdataset = pd.read_csv('2018-2010_import.csv')

#function to clean the data
def dataclean(dataset):
    dataset_dropna= dataset.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    return dataset_dropna

#cleaned the dataset
import_dropna = dataclean(importdataset)


df_all_years = import_dropna.groupby('year').agg({'value':'sum'})
print(df_all_years)

X = np.array(import_dropna['year'].unique())
y = np.array(df_all_years)


print(y)
print(X)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors = 2)
# Fit the classifier to the data
knn.fit(X_train,y_train)

#show first 5 model predictions on the test data
knn.predict(X_test)

#check accuracy of our model on the test data
knn.score(X_test, y_test)
