# Get the number from the user
number = int(input("Enter a number to print its multiplication table: "))

# Define the range for the multiplication table (1 to 10)
print(f"\nMultiplication Table for {number}:\n")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
