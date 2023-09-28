# Original lists
list1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
list2 = [1, 1, 2, 4, 5, 6]

# Calculate the difference between the two lists
difference = [item for item in list1 if item not in list2]

# Print the difference
print("Difference between two lists including duplicate elements:")
print(difference)
