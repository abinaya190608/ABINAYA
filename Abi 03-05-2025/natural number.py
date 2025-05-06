# 1. Number Series: Squares of the first n natural numbers
def square_series(n):
    print("Square Series:")
    for i in range(1, n + 1):
        print(f"{i}^2 = {i**2}")
    print()

# 2. Number Pattern: Right-angled triangle pattern of numbers
def number_pattern(n):
    print("Number Pattern:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
    print()

# 3. Pyramid Pattern: Centered star pyramid
def pyramid_pattern(n):
    print("Pyramid Star Pattern:")
    for i in range(1, n + 1):
        # Print spaces then stars
        print(' ' * (n - i) + '* ' * i)
    print()

# Main program
def main():
    try:
        n = int(input("Enter a positive integer (number of terms/rows): "))
        if n <= 0:
            print("Please enter a number greater than 0.")
            return

        square_series(n)
        number_pattern(n)
        pyramid_pattern(n)

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the program
main()
