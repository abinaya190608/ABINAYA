# Function to print numbers in ascending order
def print_ascending(start, end):
    print("Ascending Order:")
    for i in range(start, end + 1):
        print(i, end=" ")

# Function to print numbers in descending order
def print_descending(start, end):
    print("\nDescending Order:")
    for i in range(end, start - 1, -1):
        print(i, end=" ")

# Main execution
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Call functions to print in ascending and descending order
print_ascending(start, end)
print_descending(start, end)
