#Convert the input string to lowercase and remove spaces
def is_palindrome(s):
    cleaned_string = ''.join(s.lower().split())
    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
