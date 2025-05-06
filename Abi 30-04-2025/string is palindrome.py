def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    
    # Check if the string is the same forward and backward
    return s == s[::-1]

# Example usage:
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
