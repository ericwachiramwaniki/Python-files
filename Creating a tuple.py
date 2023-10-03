#Creating a tuple with different data types
my_tuple = (1, "hello", 3.14, True)

# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with a single element (remember the comma)
single_element_tuple = (42,)

# Accessing tuple elements
print("Tuple elements:")
for item in my_tuple:
    print(item)

# Accessing tuple elements by index
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])

# Tuple slicing
subset_tuple = my_tuple[1:3]
print("Subset tuple:", subset_tuple)
