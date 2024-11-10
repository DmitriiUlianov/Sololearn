import numpy as np
arr1 = np.array([[0,1],[1,2],[2,3]]) # The array arr1 is a 2-dimensional NumPy array created with the elements [[0,1],[1,2],[2,3]].
arr2 = [[0,1],[1,2],[2,3]]
print(arr1)
print("shape is ", arr1.shape) # The shape attribute of a NumPy array provides the dimensions of the array in the format (rows, columns).
print(arr2)

[[0 1]
 [1 2]
 [2 3]]
shape is  (3, 2)
[[0, 1], [1, 2], [2, 3]]

'''
The main difference between arr1 and arr2 is their data type and the operations they support.

1. Data Type:
arr1 is a NumPy array (of type numpy.ndarray), created using np.array. 
ndarray stands for "N-dimensional array" and is the core data structure in the NumPy library. 
It represents a multi-dimensional, fixed-size array of items, typically used for storing numerical data but capable of storing other data types as well.
arr2 is a Python list of lists, a standard nested list in Python.

2. Performance:
NumPy arrays (arr1) are more memory-efficient and generally much faster for numerical operations because they are stored in contiguous memory locations 
and leverage optimized C-based implementations.
Lists of lists (arr2) are less memory-efficient and slower for large-scale numerical computations.

3. Element-wise Operations:
NumPy arrays support element-wise operations. For example, arr1 * 2 would multiply each element by 2.
Lists do not support element-wise operations directly. arr2 * 2 would repeat the entire list: [[0,1],[1,2],[2,3], [0,1],[1,2],[2,3]].

4. Array Operations and Functions:
arr1 can use many NumPy functions (e.g., np.sum(arr1), np.mean(arr1), etc.), which are optimized for fast calculations on arrays.
arr2 does not have access to these functions natively. You’d need to convert it to a NumPy array first or use nested loops or list comprehensions for similar operations.

5. Shape and Indexing:
NumPy arrays have the shape attribute, which shows the dimensions of the array (e.g., (3, 2) for arr1). This makes it easy to work with multidimensional data.
Lists of lists do not have a shape attribute. You would need to check each nested list manually.

'''
