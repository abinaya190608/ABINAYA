my_dict = {'a': [1, 2, 2, 3], 'b': [1, 3, 3], 'c': [2, 2, 4]}
frequency_dict = {}
for key, value_list in my_dict.items():
    for value in value_list:
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1
print("Frequency of all elements:", frequency_dict)
