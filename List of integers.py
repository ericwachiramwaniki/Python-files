# Use a list comprehension to filter even numbers
def filter_even_numbers(input_list):
    # Use a list comprehension to filter even numbers
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

input_list = [13, 12, 93, 41, 57, 86, 107, 188, 999, 130]
result = filter_even_numbers(input_list)
print("List of even numbers:", result)
