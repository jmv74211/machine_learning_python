
# Linear regresion

It is a statistical method that allows us to summarize and study the relationships between two continuous quantitative variables.

## Introduction

Linear regression is a parametric technique **used to predict continuous dependent variables**, given a set of independent variables.

It is parametric in nature because it makes certain assumptions based on the data set.

Mathematically, the regression uses a linear function to approximate or predict a given dependent variable such as:

```
y = ax +b
```

Where:
  - "y" is the dependent variable or variable to predict.
  - "x" is the independent variable or the variable we use to make the prediction.
  - "a" is the slope and is known as the coefficient.
  - "b" is the constant that must be determined and is known as an intersection, because when "x" is equal to 0, then "y" = "b"

Simple linear regression only involves an independent variable (x).

The goal of linear regression is to **minimize the vertical distance between all data and our line**, therefore, to determine the best line
we must minimize this distance.

<p align="center">
<img src="https://raw.githubusercontent.com/jmv74211/machine_learning_python/master/doc/images/linear_regresion/example_1.png" width="70%">
</p>

One way in which the regression model finds the best line of fit is to use the least `least squares criterion` to reduce the error.

The least squares technique tries to reduce the sum of errors squared, looking for the best possible value of the regression coefficients.

**Assumptions of the linear regression technique**

- There is a linear and additive relationship between dependent and independent variables.

- There should be no correlation between independent variables, in this case it becomes extremely difficult for the model to determine the true value of the independent variables over the dependent variables.

- The error terms must have constant variance.

- The dependent variable and the error terms must have a normal distribution.

The presence of these assumptions makes the regression quite restrictive, that is, the performance of a regression model is conditioned on compliance with these assumptions.

## Use with scikit learn

```
from sklearn import linear_model

x_train = variables_independientes_entrenamiento
y_train = variables_dependientes_entrenamiento
x_test = variables_independientes_prueba
y_test = variables_dependientes_prueba

algorithm = linear_model.LinearRegression()
algorithm.fit(x_train, y_train)
algorithm.predict(x_test)
```

[See parameters in documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

**Obtaining the coefficients**

`y = ax +b`

```
a = algorithm.coef_
```

```
b = algorithm.intercept_
```

**Algorithm Performance Evaluation**

```
precision = algorithm.score(x_train, y_train)
```