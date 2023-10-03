# Function to count elements until a tuple is encountered
def count_elements_until_tuple(input_list):
    count = 0
    for item in input_list:
        if isinstance(item, tuple):
            break
        count += 1
    return count

if __name__ == "__main__":
    # Sample list
    input_list = [1, 2, 3, (4, 5), 6, 7, 8]
    # Count elements until a tuple is encountered
    count = count_elements_until_tuple(input_list)
    print("Number of elements until a tuple is encountered:", count)
