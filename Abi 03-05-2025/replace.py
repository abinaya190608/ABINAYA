string = input("Enter a string to reverse: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)


string = input("Enter a string: ")
char = input("Enter character to count its occurrences: ")
count = string.count(char)
print(f"The character '{char}' appears {count} times in the string.")


string = input("Enter a string: ")
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")
modified_string = string.replace(old_char, new_char)
print(f"Modified string: {modified_string}")
