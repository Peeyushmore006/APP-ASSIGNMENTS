
# Experiment 13: Multithreading

import threading

# Task 1: Count numbers
def count_numbers():

    for i in range(1, 6):
        print("Number:", i)


# Task 2: Calculate squares
def calculate_squares():

    for i in range(1, 6):
        print("Square of", i, "=", i * i)


# Task 3: Calculate cubes
def calculate_cubes():

    for i in range(1, 6):
        print("Cube of", i, "=", i * i * i)


# Create three threads
t1 = threading.Thread(target=count_numbers)

t2 = threading.Thread(target=calculate_squares)

t3 = threading.Thread(target=calculate_cubes)


# Start all threads
t1.start()
t2.start()
t3.start()


# Wait for all threads to complete
t1.join()
t2.join()
t3.join()

print("\nAll tasks completed!")
