# Function to print the right-angled triangle
def print_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

# Input for the height of the triangle
height = int(input("Enter the height of the triangle: "))

# Print the pattern
print_triangle(height)
