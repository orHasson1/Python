"""This program takes a list and makes a new list that has only the even elements of this list in it."""
# a: A list of numbers.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# new list: A list that receives all the even numbers of list a.
new_list = [num for num in a if num % 2 == 0]
print(new_list)