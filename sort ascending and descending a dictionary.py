# Sample dictionary
my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}

# Sort the dictionary by values in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort the dictionary by values in descending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Print the sorted dictionaries
print("Sorted by values in ascending order:")
print(sorted_dict_asc)

print("\nSorted by values in descending order:")
print(sorted_dict_desc)


