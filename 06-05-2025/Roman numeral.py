num = int(input("Enter an integer (1 - 3999): "))
if num < 1 or num > 3999:
    print("Please enter a number between 1 and 3999.")
else:
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    roman_numeral = ""
    i = 0
    while num > 0:
        count = num // val[i]
        roman_numeral += syms[i] * count
        num -= val[i] * count
        i += 1
    print("Roman numeral:", roman_numeral)
