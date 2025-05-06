# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Function to count total number of characters in a string
def count_characters(s):
    return len(s)

# Function to replace characters in a string
def replace_characters(s, old_char, new_char):
    return s.replace(old_char, new_char)

# Main function to interact with the user
def main():
    # Take input from the user
    user_string = input("Enter a string: ")
    
    # Reverse the string
    reversed_str = reverse_string(user_string)
    print(f"Reversed String: {reversed_str}")

    # Count total number of characters
    char_count = count_characters(user_string)
    print(f"Total Characters: {char_count}")

    # Replace characters
    old_char = input("Enter character to replace: ")
    new_char = input("Enter replacement character: ")
    replaced_str = replace_characters(user_string, old_char, new_char)
    print(f"String after replacement: {replaced_str}")

# Run the program
main()
