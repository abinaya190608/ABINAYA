def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return abs(a * b) // gcd

# Main function
def main():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if num1 <= 0 or num2 <= 0:
            print("Please enter positive integers only.")
            return

        gcd = find_gcd(num1, num2)
        lcm = find_lcm(num1, num2)

        print(f"GCD of {num1} and {num2} is: {gcd}")
        print(f"LCM of {num1} and {num2} is: {lcm}")

    except ValueError:
        print("Invalid input. Please enter integers only.")

# Run the program
main()
