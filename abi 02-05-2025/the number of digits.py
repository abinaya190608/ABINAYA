def is_armstrong(num):
    # Convert number to string to easily find the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return sum_of_powers == num

# Example usage
input_num = int(input("Enter a number: "))
if is_armstrong(input_num):
    print(f"{input_num} is an Armstrong number.")
else:
    print(f"{input_num} is not an Armstrong number.")
