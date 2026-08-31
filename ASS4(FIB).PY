# ============================================================
# Experiment 4
# Title: Calculate the nth Fibonacci Number Efficiently
# ============================================================

# ------------------------------------------------------------
# Function: fibonacci_iterative()
# Purpose:
#     Calculate the nth Fibonacci number using an iterative
#     dynamic programming approach.
#
# Time Complexity:  O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------

def fibonacci_iterative(n):
    # Base case: F(0) = 0
    if n == 0:
        return 0

    # Base case: F(1) = 1
    elif n == 1:
        return 1

    # 'a' stores the previous Fibonacci number
    # 'b' stores the current Fibonacci number
    a, b = 0, 1

    # Calculate Fibonacci numbers from F(2) to F(n)
    for _ in range(2, n + 1):

        # Calculate the next Fibonacci number
        c = a + b

        # Move the values forward
        a = b
        b = c

    # 'b' contains F(n)
    return b


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

def main():

    print("=" * 55)
    print("       NTH FIBONACCI NUMBER CALCULATOR")
    print("=" * 55)

    # Take input from the user
    try:
        n = int(input("\nEnter the value of n: "))

        # Fibonacci sequence is defined for non-negative
        # integer values of n.
        if n < 0:
            print("\nError: Please enter a non-negative integer.")
            return

    except ValueError:
        print("\nError: Please enter a valid integer.")
        return

    # Calculate the nth Fibonacci number
    result = fibonacci_iterative(n)

    # Display the result
    print("\n---------------------------------------------")
    print(f"Fibonacci number F({n}) = {result}")
    print("---------------------------------------------")

    # Display complexity
    print("\nTime Complexity  : O(n)")
    print("Space Complexity : O(1)")


# ------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------
# This ensures that main() is executed only when this file
# is run directly.
# ------------------------------------------------------------

if __name__ == "__main__":
    main()