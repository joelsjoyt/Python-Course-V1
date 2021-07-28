"""
This part describes about the 
different data structures in Python
"""

"""
List
    Syntax:
        list1 = [1,2,3,4,5,....n]
"""

list1 = [1,2,3,4]
print(list1)

list2 = [1,"Hello", True, 19.8]
print(list2)
print(f'Size of list2: {len(list2)} ')
print(f'Element at 2nd Index i.e index 1: {list2[1]}')


# Print list via for loop - method 1
for i in list2:
    print(i)

# Print list via for loop - method 2
for i in range(len(list2)):
    print(list2[i])

# Append/add and element to list
list2.append('World')
print(list2)

print(f'The whole list: {list2[:]}')
print(f'List from 1st - 2nd index: {list2[1:3]}')
print(f'List from 1st - end of list: {list2[1:]}')
print(f'List from 0th - 3rd index of list: {list2[:4]}')

# Remove an element from list
list2.pop(2)
print(list2)
list2.pop(3)
print(list2)

# 1-10
# calulate length
# add "World", True, 30.0
# Extract element at 8th position
# 5th pos - 11th pos
# 6th pos  - end of list
# 1st pos - 7th pos


