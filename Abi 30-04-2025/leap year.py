def is_leap_year(year):
    # Leap year if divisible by 4 but not by 100,
    # except if divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input from user
year = int(input("Enter a year: "))

# Check and display result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
