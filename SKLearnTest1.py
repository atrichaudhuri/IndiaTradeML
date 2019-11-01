from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import ImportDataPlots
targetprereshape = ImportData2018['value']
target = targetprereshape.reshape(-1,1)
features = ImportData2018['HSCode']
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=10)


# create the model
regressor_model = RandomForestRegressor(random_state=0)

# fit the model
regressor_model.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regressor_model.predict(X_test)