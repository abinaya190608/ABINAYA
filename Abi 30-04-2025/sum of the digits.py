# Function to calculate the sum of digits
def sum_of_digits(number):
    # Initialize sum to 0
    total = 0
    
    # Loop through each digit of the number
    while number > 0:
        total += number % 10  # Add the last digit to total
        number //= 10  # Remove the last digit
    
    return total

# Input: Ask user for a number
number = int(input("Enter a number: "))

# Output: Display the sum of digits
print(f"The sum of the digits is: {sum_of_digits(number)}")
