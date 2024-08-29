import numpy as np
import math

a = np.array([1, 2, 3, 4, 5, 6])

print(a)

b = a[3:]  # b is a view
print(b)

b[0] = 40

print(a)

# Dimensions, shape and size
print(a.ndim)
print(a.shape)
print(a.size)

print(len(a.shape) == a.ndim)
print(a.size == math.prod(a.shape))

# Create an array with a range of elements
range_arr = np.arange(5)
print(range_arr)


# Sorting
arr = np.array([2, 6, 1, 7, 5, 4, 3])
print(np.sort(arr))

# Concatenate two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

print(np.concatenate((arr1, arr2)))

# Reshaping an array

in_arr = np.arange(6)
print(in_arr)

in_arr = in_arr.reshape(3, 2)
print(in_arr)
