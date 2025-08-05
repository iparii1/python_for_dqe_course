import random

# Generate a random number of dictionaries (from 2 to 10)
lists_number = random.randint(2, 10)
# Initialize a list to hold the dictionaries
dict_list = []
# Create a random list of dictionaries with random letters as keys and random numbers as values
for a in range(lists_number):
    letters = 'abcdefghijklmnopqrstuvwxyz'  # Possible keys are lowercase English letters
    n = random.randint(2, 10)  # Random number of items in the dictionary (from 2 to 10)
    letters = random.sample(letters, n)  # Randomly select n unique letters as keys
    numbers = random.choices(range(100), k=n)  # Randomly generate n values in the range 0-100
    my_dict = {}
    for i in range(n):
        my_dict[letters[i]] = numbers[i]  # Create dictionary with keys as letters and values as numbers
    dict_list.append(my_dict)  # Append the generated dictionary to the list

# Initialize a temporary dictionary to hold intermediate results during merging
temporary_dict = {}

# Iterate through the list of dictionaries to populate temporary_dict
for j in range(lists_number):
    for key, value in dict_list[j].items():

        # If the key is not in temporary_dict, add it with the value, dict index, and status as single
        if key not in temporary_dict.keys():
            temporary_dict[key] = [value, j + 1, 'single']

        # If the key already exists in temporary_dict
        elif key in temporary_dict.keys() and temporary_dict[key][0] >= dict_list[j][key]:
            # Mark item as 'duplicate' if the value in the temporary_dict is greater
            temporary_dict[key][2] = 'duplicate'
        else:
            # If the value in the current dictionary is greater, update with the larger value and mark as 'duplicate'
            temporary_dict[key] = [value, j + 1, 'duplicate']

# Initialize merged dictionary
merged_dict = {}

# Populate the final merged dictionary from temporary_dict
for key, value in temporary_dict.items():
    # If the key is marked as 'single', keep it as it is
    if temporary_dict[key][2] == 'single':
        merged_dict[key] = temporary_dict[key][0]
    else:
        # If the key is marked as 'duplicate', add dictionary index to the key
        new_key = key + '_' + str(temporary_dict[key][1])
        merged_dict[new_key] = temporary_dict[key][0]

print(merged_dict)