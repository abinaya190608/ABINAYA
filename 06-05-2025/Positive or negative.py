positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    elif num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1
if positive_count > 0:
    positive_avg = round(positive_sum / positive_count, 2)
    print("Average of positive numbers:", positive_avg)
else:
    print("No positive numbers entered.")
if negative_count > 0:
    negative_avg = round(negative_sum / negative_count, 2)
    print("Average of negative numbers:", negative_avg)
else:
    print("No negative numbers entered.")
