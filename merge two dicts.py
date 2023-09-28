# Define two dictionaries
dict1 = {'a': 10, 'b': 20}
dict2 = {'b': 30, 'c': 40}

# Merge dict2 into dict1 using the ** operator
merged_dict = {**dict1, **dict2}

# Print the merged dictionary
print(merged_dict)
