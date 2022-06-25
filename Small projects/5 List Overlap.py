"""This program returns a list that contains only the elements that are common between two random lists lists."""
import random
# a: A list receives random numbers.
a = []
# b: A list receives random numbers.
b = []
# a_len: A random length for list a.
a_len = random.randint(1, 10)
# b_len: A random length for list b.
b_len = random.randint(1, 10)

for num1 in range(1, a_len + 1):
    num1 = random.randint(0, 20)
    a.append(num1)

for num in range(1, b_len + 1):
    num = random.randint(0, 20)
    b.append(num)

# new_list: A list that receives all the overlap numbers of lists a and b.
new_list = list(set(a).intersection(b))
print("List a:", a, "\n", "List b:", b, "\n", "New list:", new_list)