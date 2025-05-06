# Program to find the largest of three numbers

# Input three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Find the largest using if-elif-else
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Display the result
print("The largest number is:", largest)
