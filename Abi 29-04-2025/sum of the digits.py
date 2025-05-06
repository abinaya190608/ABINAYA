def sum_of_digits(number):
    # Ensure the number is positive
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10  # Add the last digit
        number //= 10         # Remove the last digit
    return total

# Example usage
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
