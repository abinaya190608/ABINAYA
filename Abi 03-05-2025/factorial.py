import math

# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Function to find the largest number in a list
def find_largest(numbers):
    if not numbers:
        return "Error: List is empty"
    return max(numbers)

# Function to calculate area based on shape
def area_of_shape(shape, *args):
    if shape == "circle" and len(args) == 1:
        radius = args[0]
        return math.pi * radius * radius
    elif shape == "rectangle" and len(args) == 2:
        length, width = args
        return length * width
    elif shape == "triangle" and len(args) == 2:
        base, height = args
        return 0.5 * base * height
    else:
        return "Error: Invalid shape or arguments"

# Example usage:
print("Factorial of 5:", factorial(5))

my_list = [3, 10, 2, 8, 6]
print("Largest number in list:", find_largest(my_list))

print("Area of circle (r=3):", area_of_shape("circle", 3))
print("Area of rectangle (4x5):", area_of_shape("rectangle", 4, 5))
print("Area of triangle (base=6, height=2):", area_of_shape("triangle", 6, 2))
