def even_square_series(n):
    print("Even numbers and their squares:")
    for i in range(1, n+1):
        even = i * 2
        print(f"{even}^2 = {even ** 2}")
def number_triangle(n):
    print("\nNumber Triangle Pattern:")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
def star_pyramid(n):
    print("\nPyramid Star Pattern:")
    for i in range(1, n+1):
        print(' ' * (n - i) + '* ' * i)
