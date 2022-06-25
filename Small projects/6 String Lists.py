"""The program asks the user for a string and print out whether this string is a palindrome or not."""
# chosen_str: A latter given by the user (converted to a list of letters).
chosen_str = list(input("Enter a word:"))
# reverse_chosen_str: The reverse list of chosen_str.
reverse_chosen_str = list(reversed(chosen_str))
if chosen_str == reverse_chosen_str:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome!")




