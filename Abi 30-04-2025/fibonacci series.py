def fibonacci_series(n):
    # Initialize the first two terms
    a, b = 0, 1
    
    # Check if the input is less than or equal to 0
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print(f"Fibonacci series up to {n} term: {a}")
    else:
        print(f"Fibonacci series up to {n} terms: ", end="")
        # Print the first two terms
        print(a, end=" ")
        for _ in range(2, n):
            a, b = b, a + b
            print(a, end=" ")
        print()

# Input from the user
n = int(input("Enter the number of terms: "))
fibonacci_series(n)
