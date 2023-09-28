# Original list of strings
original_list = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']

# Convert the strings to integers using list comprehension
numeric_list = [int(x) for x in original_list]

# Sort the numeric list
sorted_list = sorted(numeric_list)

# Print the sorted list
print("Sort the said list of strings(numbers) numerically:")
print(sorted_list)
