"""This program prints out all the elements of a list that are less than 5."""
# a: A list of numbers.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# new_list: A list that receives all the elements of list a that are smaller than 5.
new_list = list()
for num in a:
    if num < 5:
        new_list.append(num)
print(new_list)

