
# Experiment 15: Garbage Collection

import gc
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Function to display memory usage
def show_memory():

    current, peak = tracemalloc.get_traced_memory()

    print("Current Memory:",
          current, "bytes")

    print("Peak Memory:",
          peak, "bytes")


# Display initial memory usage
print("Initial Memory Usage:")
show_memory()


# Create objects with circular references
def create_objects():

    objects = []

    for i in range(1000):

        # Create an empty list
        obj = []

        # Create circular reference
        obj.append(obj)

        objects.append(obj)

    return objects


# Create objects
data = create_objects()

print("\nAfter Creating Objects:")
show_memory()


# Delete references
del data

print("\nAfter Deleting Objects:")
show_memory()


# Manually collect garbage
collected = gc.collect()

print("\nGarbage Collection:")
print("Objects collected:", collected)


# Display memory after garbage collection
print("\nAfter Garbage Collection:")
show_memory()


# Display garbage collection thresholds
print("\nGC Thresholds:")
print(gc.get_threshold())


# Stop memory tracking
tracemalloc.stop()
