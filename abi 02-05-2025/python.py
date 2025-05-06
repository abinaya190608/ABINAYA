def sum_of_squares(n):
    # Calculate the sum of squares using the formula: n(n+1)(2n+1) / 6
    return n * (n + 1) * (2 * n + 1) // 6

# Input: Read the value of n
n = int(input("Enter a number n: "))

# Output: Print the sum of squares
print(f"The sum of squares of the first {n} natural numbers is: {sum_of_squares(n)}")
