
# Experiment 11: Pandas Series

import pandas as pd
import numpy as np

# Generate 10 random numbers
numbers = np.random.randint(1, 100, 10)

# Create a Pandas Series
series = pd.Series(numbers)

# Display the Series
print("Pandas Series:")
print(series)


# Access element using index
print("\nElement at index 2:", series[2])


# Display first five elements
print("\nFirst five elements:")
print(series.head())


# Filter numbers greater than 50
print("\nNumbers greater than 50:")
print(series[series > 50])


# Calculate statistical values
print("\nMean:", series.mean())

print("Median:", series.median())

print("Minimum:", series.min())

print("Maximum:", series.max())
