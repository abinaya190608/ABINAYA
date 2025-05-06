def reverse_number(n):
    reversed_num = int(str(n)[::-1]) if n >= 0 else -int(str(abs(n))[::-1])
    return reversed_num
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print(f"Reversed number: {reversed_num}")
