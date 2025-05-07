def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        hanoi(n - 1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, auxiliary, source, target)
num_disks = int(input("Enter the number of disks: "))
print("The sequence of moves is:\n")
hanoi(num_disks, 'A', 'B', 'C')
