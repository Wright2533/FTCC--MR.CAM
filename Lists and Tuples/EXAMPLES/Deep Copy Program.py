# How to make a shallow copy of a list

list_one = [1, 2, 3, 4, 5]
list_two = list_one
list_two[1] = 4
print(list_one)
print(list_two)

#How to make a deep copy of a list

import copy
list_one = [1, 2, 3, 4, 5]
list_two = copy.deepcopy(list_one)
list_two[1] = 4
print(list_one)
print(list_two)
