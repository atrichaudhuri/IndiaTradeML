import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#function to clean the data
def dataclean(df):
    dataset_dropna = df.dropna(inplace=False)
    return dataset_dropna

def RegPredict(df):

    #sum of values for each year
    values = df.groupby('year').agg({'value' : 'sum'})
    print(values)

    #array of years assigned to X and array of values assigned to y
    X = [[2010],[2011],[2012],[2013],[2014],[2015],[2016],[2017],[2018]]
    y = np.array(values)

    #printing X and y to validate data
    print("The Y Array is\n" , y)
    print("The X Array is\n" , X)

    #importing train_test_split to split the data (Test = 20%, Training = 80%)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 , random_state = 10)

    #importing Linear Regression module from sklearn
    from sklearn.linear_model import LinearRegression

    #modelling
    reg = LinearRegression().fit(X , y)
    #predicting against test set
    y_pred = reg.predict(X_test)
    #comparing actual and predicted values
    pred_comparison = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})

    print("Prediction Comparison", pred_comparison)
    print("R Squared Score" , reg.score(X,y))

    plt.plot(X_test, y_test, color='gray')
    plt.plot(X_test, y_pred, color='red', linewidth=2)

    print("Prediction for 2019\n", reg.predict([[2019]]))
    print("Prediction for 2020\n", reg.predict([[2020]]))
    print("Prediction for 2021\n", reg.predict([[2021]]))
    print("Prediction for 2022\n", reg.predict([[2022]]))
    print("Prediction for 2023\n", reg.predict([[2023]]))

    pred_grp = reg.predict([[2019],[2020], [2021], [2022], [2023]])
    pred_years= [[2019], [2020], [2021], [2022], [2023]]
    pred_plot = plt.scatter(X, y, color = 'gray')
    pred_plot = plt.plot(pred_years,pred_grp,color='red')

    plt.show()

#function calls
#importing the dataset
importdataset = pd.read_csv('2018-2010_import.csv')
print("Shape of Dataset \n", importdataset.shape)
print("Description of Dataset \n", importdataset.describe())

#cleaning the dataset
import_dropna = dataclean(importdataset)

#running the prediction and visualising
RegPredict(import_dropna)

