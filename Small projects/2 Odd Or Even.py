"""This program asks the user for a number. Depending on whether the number is even or odd, it prints out an appropriate
message."""
# chosen_num: A number given by the user.
chosen_num = int(input("Enter a number: "))
if (chosen_num % 2) == 0:
    print("The number is even.")
else:
    print("The number is odd.")


