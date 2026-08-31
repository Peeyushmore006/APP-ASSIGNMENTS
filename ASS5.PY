# ============================================================
# Experiment No. 5
# Title: Longest Common Subsequence (LCS)
# ============================================================

# ------------------------------------------------------------
# Function: find_lcs()
# Purpose:
#     Find the Longest Common Subsequence between two strings
#     using Dynamic Programming (Bottom-Up / Tabulation).
#
# Parameters:
#     X - First sequence
#     Y - Second sequence
#
# Returns:
#     The LCS string and its length
#
# Time Complexity:  O(m * n)
# Space Complexity: O(m * n)
# ------------------------------------------------------------

def find_lcs(X, Y):

    # Length of both sequences
    m = len(X)
    n = len(Y)

    # --------------------------------------------------------
    # Create a DP table.
    #
    # dp[i][j] represents the length of the LCS of:
    # X[0:i] and Y[0:j]
    #
    # We create (m+1) x (n+1) table because row 0 and
    # column 0 represent an empty sequence.
    # --------------------------------------------------------

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # --------------------------------------------------------
    # Fill the DP table using the bottom-up approach.
    # --------------------------------------------------------

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            # If current characters are equal,
            # add 1 to the diagonal value.
            if X[i - 1] == Y[j - 1]:

                dp[i][j] = dp[i - 1][j - 1] + 1

            else:

                # If characters are different, choose the
                # maximum value from the cell above or
                # the cell on the left.
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    # --------------------------------------------------------
    # Reconstruct the actual LCS string.
    #
    # Start from the bottom-right corner of the table
    # and move backwards.
    # --------------------------------------------------------

    i = m
    j = n

    lcs = []

    while i > 0 and j > 0:

        # If characters match, this character belongs
        # to the LCS.
        if X[i - 1] == Y[j - 1]:

            lcs.append(X[i - 1])

            # Move diagonally upwards.
            i -= 1
            j -= 1

        # If the value above is greater, move upward.
        elif dp[i - 1][j] > dp[i][j - 1]:

            i -= 1

        # Otherwise, move left.
        else:

            j -= 1

    # --------------------------------------------------------
    # Since we constructed the LCS backwards, reverse it
    # before returning the final result.
    # --------------------------------------------------------

    lcs.reverse()

    # Convert list of characters into a string.
    lcs_string = "".join(lcs)

    return lcs_string, dp[m][n]


# ------------------------------------------------------------
# Function: display_dp_table()
# Purpose:
#     Display the Dynamic Programming table.
#     This helps understand how the LCS is calculated.
# ------------------------------------------------------------

def display_dp_table(X, Y):

    m = len(X)
    n = len(Y)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:

                dp[i][j] = dp[i - 1][j - 1] + 1

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    # Display table heading
    print("\nDynamic Programming Table:")
    print("-" * 50)

    # Print column characters
    print("    ", end="")

    for char in Y:
        print(f"{char:4}", end="")

    print()

    # Print table rows
    for i in range(m + 1):

        if i == 0:
            print("  ", end="")
        else:
            print(f"{X[i - 1]} ", end="")

        for j in range(n + 1):

            print(f"{dp[i][j]:4}", end="")

        print()

    print("-" * 50)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 60)
    print("       LONGEST COMMON SUBSEQUENCE (LCS)")
    print("          USING DYNAMIC PROGRAMMING")
    print("=" * 60)

    # --------------------------------------------------------
    # Take two sequences from the user.
    # --------------------------------------------------------

    X = input("\nEnter first sequence: ")
    Y = input("Enter second sequence: ")

    # Remove unnecessary spaces from both sequences.
    X = X.strip()
    Y = Y.strip()

    # Check whether input is empty.
    if not X or not Y:

        print("\nError: Sequences cannot be empty.")
        return

    # --------------------------------------------------------
    # Find the LCS.
    # --------------------------------------------------------

    lcs_string, lcs_length = find_lcs(X, Y)

    # --------------------------------------------------------
    # Display results.
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("                     RESULT")
    print("=" * 60)

    print(f"First Sequence  : {X}")
    print(f"Second Sequence : {Y}")

    print(f"\nLongest Common Subsequence : {lcs_string}")
    print(f"Length of LCS              : {lcs_length}")

    print("=" * 60)

    # Display the DP table
    display_dp_table(X, Y)

    # Display complexity
    print("\nComplexity:")
    print("Time Complexity  : O(m × n)")
    print("Space Complexity : O(m × n)")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================
# The main() function is executed only when this file
# is run directly.
# ============================================================

if __name__ == "__main__":
    main()