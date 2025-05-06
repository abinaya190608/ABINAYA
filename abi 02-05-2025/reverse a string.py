def reverse_string(input_string):
    # Initialize an empty string to hold the reversed string
    reversed_string = ""
    
    # Loop through the original string in reverse order
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    
    return reversed_string

# Test the function
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
