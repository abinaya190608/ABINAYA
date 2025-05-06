def count_char_occurrences(input_string, char_to_count):
    # Use the count() method to count the occurrences of the character
    return input_string.count(char_to_count)

# Example usage
input_string = "hello world"
char_to_count = 'o'

# Call the function
occurrences = count_char_occurrences(input_string, char_to_count)
print(f"The character '{char_to_count}' appears {occurrences} times in the string.")
