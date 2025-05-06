def fibonacci_series(n):
    a, b = 0, 1
    series = []

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series

# Get input from the user
try:
    n = int(input("Enter the number of terms for Fibonacci series: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = fibonacci_series(n)
        print("Fibonacci Series:", result)

except ValueError:
    print("Invalid input. Please enter an integer.")
