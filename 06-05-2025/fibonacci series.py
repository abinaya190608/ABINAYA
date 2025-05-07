n = int(input("Enter the number of steps: "))
if n == 0 or n == 1:
    print("Number of ways:", 1)
else:
    a = 1  
    b = 1 
    for i in range(2, n + 1):
        total = a + b
        a = b
        b = total
    print("Number of ways:", b)
