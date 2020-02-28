#!/usr/bin/python3

"""
Linear regresion example code

In this example we are going to use a dataset called Boston, which we will use to be able to predict the
average cost of housing according to the number of rooms
"""

import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

# Import data from scikit-learn dataset
boston = datasets.load_boston()

"""
Output: dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename'])
"""

# Get the dataset information
print("dataset info:")
print(boston.keys())

# Verify the dataset features
print("dataset features:")
print(boston.DESCR)

# See the data volume
print("data volume:")
print(boston.data.shape)

# Verify the column names
print("data column names")
print(boston.feature_names)

# Take as independent variable the number of rooms (RM)
# Select only column 5 of the dataset
x = boston.data[:, np.newaxis, 5]

# Define the data for the labels
y = boston.target

# Plot the data using dispersion
plt.scatter(x,y)
plt.xlabel('number of rooms')
plt.ylabel('Average value')
plt.show()

# Separate training and test data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Define the algorithm to be used
lr = linear_model.LinearRegression()

# Train the model
lr.fit(x_train, y_train)

# Make the prediction
y_pred = lr.predict(x_test)

# Plot the data and model
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, color='red', linewidth=3)
plt.title('Linear regresion')
plt.xlabel('Number of rooms')
plt.ylabel('Average value')
plt.show()

# Calculate the value of the slope and intersection
print("a = {}".format(lr.coef_))
print("b = {}".format(lr.intercept_))

"""
Output:
a = 8.6623
b = -31.9950
"""

# Calculate the accuracy of the algorithm
print("accuracy of the algorithm:")
print(lr.score(x_train, y_train))

"""
Output:
0.4580
"""

# In this case we can say that this algorithm does not fit this data set.