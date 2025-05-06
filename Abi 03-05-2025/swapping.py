# Swapping with a temporary variable
a = 10
b = 20

print("Before swapping (with temp variable): a =", a, ", b =", b)

# Using a temporary variable
temp = a
a = b
b = temp

print("After swapping (with temp variable): a =", a, ", b =", b)

# Swapping without a temporary variable
x = 30
y = 40

print("\nBefore swapping (without temp variable): x =", x, ", y =", y)

# Pythonic way to swap without a temp variable
x, y = y, x

print("After swapping (without temp variable): x =", x, ", y =", y)
