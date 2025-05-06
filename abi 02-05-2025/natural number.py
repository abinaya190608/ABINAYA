def sum_of_natural_numbers(n):
    # Using the formula: sum = n * (n + 1) / 2
    return n * (n + 1) // 2

# Input: Take n as input
n = int(input("Enter a number: "))

# Output: Display the sum of the first n natural numbers
print("The sum of the first", n, "natural numbers is:", sum_of_natural_numbers(n))
