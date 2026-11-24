
# Experiment 10: NumPy Array Operations

import numpy as np

# Create a NumPy array from 1 to 10
arr = np.arange(1, 11)

print("Original Array:")
print(arr)


# Indexing: Access an element
print("\nElement at index 2:", arr[2])


# Slicing: Extract elements from index 2 to 5
print("Sliced Array:", arr[2:6])


# Calculate sum
print("Sum:", np.sum(arr))


# Calculate mean
print("Mean:", np.mean(arr))


# Find maximum value
print("Maximum:", np.max(arr))


# Find minimum value
print("Minimum:", np.min(arr))


# Broadcasting: Add 5 to every element
new_arr = arr + 5

print("Array after Broadcasting:")
print(new_arr)
