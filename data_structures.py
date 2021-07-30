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

"""
Tuple
    Syntax:
        list1 = (1,2,3,4,5,....n)
"""
print(list1)
list1[2] = 6
print(list1)


tuple1 = (1,2,3,4)
print(tuple1)
print(f'Element at index 2: {tuple1[2]}')
# tuple1[2] = "Hello"
print(tuple1)
print(f'The whole Tuple: {tuple1[:]}')
print(f'Tuple from 1st - 2nd index: {tuple1[1:3]}')
print(f'Tuple from 1st - end of list: {tuple1[1:]}')
print(f'Tuple from 0th - 3rd index of list: {tuple1[:4]}')


"""
Set
    Syntax:
        set1 = {1,2,3,4,5,....n}
"""

set1 = {"hello", 1, 2,3,3}
print(set1)

"""
Dictionary
    Syntax:
        dict1 = {
            "Key1":"etc",
            "Key2":123
            ....
            ....
        }
"""

dict1 = {
    "id":"i896",
    "Name":"Mark",
    "Age":25
}

# Print dictionary  method 1
print(dict1)

# Print Dictionary method 2
print(dict1.items())

# Print keys of dictionary
print(dict1.keys())

# Print values of dictionary
print(dict1.values())

# Get a value from dictionary
print(dict1["Name"])

# Iterate to a dictionary
for key in dict1.keys():
    print(f'Key: {key}, value: {dict1[key]}')

# Dictionary Updation method 1
dict1.update({'Place':"XYZ"})
print(dict1)

# Dictrionary Updation method 1
dict1.__setitem__("Country", "PQR")
print(dict1)

# Dictionary Merging
dict2 = {
    'Audit':'Pass',
    'Deployment':'Completed',
    'Update Schedule':'Pending'
}

new_dict = {**dict1, **dict2}
"""
Expansion
 new_dict ={ 
   {'id': 'i896', 'Name': 'Mark', 'Age': 25, 'Place': 'XYZ', 'Country': 'PQR'}
   {'Audit': 'Pass', 'Deployment': 'Completed', 'Update Schedule': 'Pending'}
 }
"""
print(new_dict)

# Remove an item from dictionary
new_dict.pop('Deployment')
print(new_dict)

#Clear and add values to dictionary
new_dict.clear()
print(new_dict)

new_dict = {**new_dict, **dict2}
"""
Expansion/Unpacking
 new_dict ={ 
   {'id': 'i896', 'Name': 'Mark', 'Age': 25, 'Place': 'XYZ', 'Country': 'PQR'}
   {'Audit': 'Pass', 'Deployment': 'Completed', 'Update Schedule': 'Pending'}
 }
"""
print(new_dict)

#Deletes the whole dictionary from memory
# del new_dict
# print(new_dict)

# Pops the last item from dictionary
new_dict.popitem()
print(new_dict)

# dict1
# customer id
# cust bal

# dict2
# item
# item price