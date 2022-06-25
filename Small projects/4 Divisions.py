"""This program asks the user for a number and then prints out a list of all the divisors of that number."""
# num: A number given by the user.
num = int(input("Enter a number: "))
# divisions_list: A list that receives all the divisions of the chosen number.
divisions_list = list()
for x in range(1, num + 1):
    if num % x == 0:
        divisions_list.append(x)
print(divisions_list)