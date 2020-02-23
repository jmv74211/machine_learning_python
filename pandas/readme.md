# Introduction to pandas

pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language. It provides high performance data manipulation and analysis tools. Its main functions are:

- Prepare
- Load
- Manipulate
- Model
- Analyse

---

## Dataframe

Pandas dataframe are two-dimensional tagged data structures. It consists of 3 types of components: data, indexes and columns.
You can specify the index and column names. It contains heterogeneous data, and data and size may be mutable.

---

## Use examples

### Pandas dataframe

```Python
import numpy as np
import pandas as pd

# Example of dataframe
data = np.array([['','Col1','Col2'], ['Fila1',11,22], ['Fila2',33,44]])
print(pd.Dataframe(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))

"""
Output:
        Col1  Col2
 Fila 1  11    22
 Fila 2  33    44
"""
# Example 2 of dataframe
df = pd.Dataframe(np.array([[1,2,3], [4,5,6], [7,8,9]]))
print(df)

"""
Output:
   0  1  2
0  1  2  3
1  4  5  6
2  7  8  9
"""
```

### Create series

```Python
series = pd.Series({"Argentina":"Buenos Aires",
                    "Chile":"Santiago de Chile",
                    "Colombia":"Bogotá",
                    "Perú":"Lima"})
print(series)

"""
Output:
Argentina   Buenos Aires
Chile       Santiago de Chile
Colombia    Bogotá
Perú        Lima
"""
```

### Dataframe statistics

```Python
# Print dataframe height
df = pd.Dataframe(np.array([[1,2,3], [4,5,6], [7,8,9]]))
print(len(df.index)) # Output: 3

# Data summary
print(df.describe()) # Count, mean, std, min, 25%, 50%, 75%, max

# Mean of columns
print(df.mean())

# Dataframe correlation
print(df.corr())

# Number of non-null values for each column of the dataframe
print(df.count())

# Get highest value in each column
print(df.max())

# Get lowest value in each column
print(df.min())

# Get median in each column
print(df.median())

# Get standard deviation in each column
print(df.std())
```

### Data selection

```Python
# Select the first column of the dataframe
print(df[0])

"""
Dataframe:
  0 1 2
0 1 2 3  Output: 0  1
1 4 5 6          1  4
2 7 8 9          2  7
"""

# Create a new dataframe from several columns
print(df[0, 1])

"""
Dataframe:
  0 1 2            0 1
0 1 2 3  Output: 0 1 2  
1 4 5 6          1 4 5
2 7 8 9          2 7 8
"""

#Select the value of the first row and last column
print(df.iloc[0][2])

"""
Dataframe:
  0 1 2
0 1 2 3  Output: 3
1 4 5 6
2 7 8 9
"""

# Select values from the first column
print(df.loc[0])
print(df.iloc[0,:]) # Same result

"""
Dataframe:
  0 1 2
0 1 2 3  Output: 0   1
1 4 5 6          1   2
2 7 8 9          2   3
"""
```

### Load data

```Python
# Read data
df = pd.read_csv('train.csv')
```

### Clean data

```Python
# Check if there is null data in the Dataframe
print(df.isnull())

# Get sum of null values in the dataframe
print(df.isnull().sum())

# Eliminate rows of missing values
df.dropna()

# Eliminate columns of missing values
df.dropna(axis = 1)

# Fill in missing values with another value
df.fillna(x)
```
