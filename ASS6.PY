
# Experiment 6: 0/1 Knapsack Problem

# Values (profits) of items
values = [60, 100, 120]

# Weights of items
weights = [10, 20, 30]

# Maximum capacity of the bag
W = 50

n = len(values)


# 1. Bottom-Up Approach
def knapsack_bottom_up(values, weights, W):

    n = len(values)

    # Create a DP table filled with zeros
    dp = [[0 for _ in range(W + 1)]
          for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(W + 1):

            # Check if the current item can fit
            if weights[i - 1] <= w:

                # Choose maximum profit:
                # Include item or exclude item
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] +
                    dp[i - 1][w - weights[i - 1]]
                )

            else:
                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# 2. Top-Down Approach using Memoization
def knapsack_top_down(values, weights, W):

    n = len(values)

    # Create a memoization table
    dp = [[-1 for _ in range(W + 1)]
          for _ in range(n + 1)]

    def solve(n, W):

        # Base condition
        if n == 0 or W == 0:
            return 0

        # Return already calculated result
        if dp[n][W] != -1:
            return dp[n][W]

        # If item weight is greater than capacity
        if weights[n - 1] > W:
            dp[n][W] = solve(n - 1, W)

        else:
            # Include or exclude the item
            dp[n][W] = max(
                solve(n - 1, W),
                values[n - 1] +
                solve(n - 1, W - weights[n - 1])
            )

        return dp[n][W]

    return solve(n, W)


# Display results
print("Bottom-Up Approach:",
      knapsack_bottom_up(values, weights, W))

print("Top-Down Approach:",
      knapsack_top_down(values, weights, W))
