def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_output = celsius_to_fahrenheit(celsius_input)
print(f"{celsius_input}°C is equal to {fahrenheit_output:.2f}°F")
