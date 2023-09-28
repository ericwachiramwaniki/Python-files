# Define a dictionary with numeric values
my_dict = {'a': 100, 'b': 120, 'c': 330, 'd': 640}

# Initialize a variable to store the sum
total_sum = 0

# Iterate through the values of the dictionary and add them to the total_sum
for value in my_dict.values():
    total_sum += value

# Print the sum
print("The sum of all items in the dictionary is:", total_sum)
