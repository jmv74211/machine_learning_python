# Introduction to numpy

NumPy is the fundamental package for scientific computing with Python. Its main characteristics are:

- Powerful data structure.

- Implements arrays and multidimensional arrays.

- These structures guarantee efficient calculations with arrays.

---

## NumPy array

It is a powerful N-dimensional matrix object that has the shape of rows and columns, in which we have several elements that are stored in their respective memory locations.

```Python
import numpy as np

a = np.array([1,2,3])
print("1D array: {}".format(a))

b = np.array([(1,2,3),(4,5,6)])
print("2D array: {}".format(b))
```

```
Output:
1D array: [1 2 3]

2D array: [[1 2 3]
            4 5 6]]
```

The main advantages when working with numpy are:

- NumPy array takes up **less memory space** than Python lists.

   *Example: List with 1000 items*:

 - `Python lists`: 28000B
 - `NumPy array`:  8000B


- NumPy is **faster**.

   *Example: Sum of two lists with 1.000.000 items*:

   - `Python lists`: 207ms
   - `NumPy array`:  51ms

**Conclusions**

NumPy array:

- takes up less space.
- is faster.
- is functional.

---

## Use examples

### Creation and initialization

```Python
# Create matrix 2f x 4c initialized with ones
_ones = np.ones((2,4))

"""
Output:
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
"""

 # Create matrix 3f x 4c initialized with zeros
_ceros = np.zeros((2,3))

"""
Output:
[[0. 0. 0.]
 [0. 0. 0.]]
"""

# Create matrix 2f x 2c initialized with random values
_random = np.random.random((2,2))

"""
Output:
[[0.708 0.822]
 [0.802 0.307]]
"""

# Create matrix 3f x 2c initialized with empty values
_random = np.empty((3,2))

"""
Output:
[[0. 0.]
 [0. 0.]
 [0. 0.]]
"""

# Create matrix 2f x 2c initialized with value 8.
_full = np.full((2,2),8)

"""
Output:
[[8 8]
 [8 8]]
"""

# Create matrix with evenly spaced values
_space1 = np.arange(0,30,5)

"""
Output:
[0 5 10 15 20 25]
"""

# Create matrix with evenly spaced values
_space2 = np.linspace(0,2,5)

"""
Output:
[0. 0.5 1. 1.5 2.]
"""

# Create 2f x 2c identity matrix
_identity = np.identity(2)

"""
Output:
[[1. 0.]
 [0. 1.]]
"""
```

### Inspection

```Python
# Get the dimension of a matrix
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim) # Output: 2

# Get data type
print(a.dtype) # Output: int64

# Get data size and shape
a = np.array([(1,2,3,4,5,6)])
print(a.size) # Output: 6
print(a.shape) # Output: (1,6)
```

### Matrix size and shape changes

```Python
a = np.array([(8,9,10),(11,12,13)])
print(a)

"""
Output:
[[ 8 9 19]
 [11 12 13]]
"""

# Changing the shape of a matrix
a = a.reshape(3,2)
print(a)

"""
Output:
[[ 8 9]
 [10 11]
 [12 13]]
"""
```

### Access to the matrix elements

```Python
# Get the value of row 0 column 2
a = np.array([(1,2,3,4),(3,4,5,6)])
print(a[0,2]) # Output: 3

# Get all the values from the row in column 3
print(a[0:,2]) # Output [3 5]
```
### Mathematical operations between arrays

```Python
# Find min, max and sum
a = np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())

# Square root and typical deviation
a = np.array([(1,2,3),(3,4,5)])

# Square root
print(np.sqrt(a))

# typical deviation
print(np.std(a))

# basic operations

x = np.array([(1,2,3),(3,4,5)])
y = np.array([(1,2,3),(3,4,5)])

print(x+y) # Sum
print(x-y) # Subtraction
print(x*y) # Multiplication
print(x/y) # Division
```
