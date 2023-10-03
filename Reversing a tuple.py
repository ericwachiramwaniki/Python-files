# Function to reverse a tuple
def reverse_tuple(input_tuple):
    reversed_tuple = input_tuple[::-1]
    return reversed_tuple

# Example usage
if __name__ == "__main__":
    # Sample tuple
    original_tuple = (1, 2, 3, 4, 5)
    # Reversing the tuple
    reversed_tuple = reverse_tuple(original_tuple)
    print("Original Tuple:", original_tuple)
    print("Reversed Tuple:", reversed_tuple)





