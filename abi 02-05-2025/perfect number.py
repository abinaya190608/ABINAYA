def is_perfect_number(num):
    if num <= 1:
        return False
    
    # Find divisors and calculate their sum
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    
    # Check if sum of divisors equals the number
    return sum_of_divisors == num

# Input from user
number = int(input("Enter a number: "))

# Check if the number is perfect
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
