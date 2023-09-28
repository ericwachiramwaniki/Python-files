# Define a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Specify the key you want to remove
key_to_remove = 'b'

# Check if the key is in the dictionary before removing it
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
    print(f"The key '{key_to_remove}' has been removed from the dictionary.")
else:
    print(f"The key '{key_to_remove}' is not in the dictionary.")

# Print the updated dictionary
print("Updated dictionary:", my_dict)
