"""This program asks the user to enter his name, age and a chosen number. It prints copies of a sentence that tells
the year that the user will turn 100, as many as the chosen number."""
# name: The name given by the user.
name = input("Enter your name: ")
#  age: The age given by the user.
age = int(input("Enter your age: "))
# when_100: The year that the user will turn 100 years old.
when_100 = str(2019 - age + 100)
# message: A sentence that tells the year that the user will turn 100.
message = name + " You will turn 100 by " + when_100 + "."
# chosen_num: Number given by the user.
chosen_num = int(input("Enter a number: "))
print((message + "\n") * chosen_num)
