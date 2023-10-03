# Creating an empty set
empty_set = set()

# Creating a set with elements
my_set = {1, 2, 3, 4, 5}

# Creating a set from a list
my_list = [1, 2, 3, 4, 5]
set_from_list = set(my_list)

# Creating a set from a tuple
my_tuple = (1, 2, 3, 4, 5)
set_from_tuple = set(my_tuple)

# Creating a set with mixed data types
mixed_set = {1, "hello", 3.14, (1, 2, 3)}

# Adding elements to an existing set
my_set.add(6)
my_set.update([7, 8, 9])

# Removing elements from a set
my_set.remove(3)
# Raises KeyError if the element is not found
my_set.discard(10)
# Does not raise an error if the element is not found

# Iterating through a set
for element in my_set:
    print(element)

# Checking if an element is in the set
if 6 in my_set:
    print("6 is in the set")

# Finding the length of a set
set_length = len(my_set)

# Creating a copy of a set
set_copy = my_set.copy()

# Clearing all elements from a set
my_set.clear()

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)

# Intersection of sets
intersection_set = set1.intersection(set2)

# Difference of sets
difference_set = set1.difference(set2)

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)

# Subset and Superset
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)
