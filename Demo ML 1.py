import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
# Assuming three decision variables x1, x2, x3 and additional parameters
X = np.random.rand(100, 3) * 10  # Decision variables between 0 and 10
params = np.random.rand(100, 2) * 5  # Additional parameters
cost_function = 2*X[:, 0] + 3*X[:, 1] - 4*X[:, 2] + params[:, 0] - params[:, 1] + np.random.randn(100) * 5

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(np.concatenate((X, params), axis=1), cost_function, test_size=0.2, random_state=42)

# Create and train a regression model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plot the results (for visualization purposes, you may need to choose which variables to plot)
plt.scatter(X_test[:, 0], y_test, color='black', label='Actual Costs')
plt.scatter(X_test[:, 0], y_pred, color='blue', label='Predicted Costs')
plt.xlabel('Decision Variable x1')
plt.ylabel('Cost Function')
plt.legend()
plt.show()
