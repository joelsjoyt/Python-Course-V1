# Lists syntax
# variable  = [ Element1, element 2,....element n]

a = [1,2,3,4,5]
# #print(type(a))
# #print(len(a))

# #1 -> 0 index
# #2 -> 1 index
# #n -> n-1 index

# #print(a[2]) get an element
# #print( a[0:3] )

# #[0,1,2,....,n-1] index of elements
# #0....3

# # for i in range(len(a)):
# #     print(a[i])

# b = ["hello", True, 12, 12.5]

# c = a + b #concatination 
# print(len(c))

# a = list(range(1,6))
# print(a)

# Tuples syntax
# [1,2,1,3,5,5]
# (1, 1, 2, 3, 4) => (1, 2, 3 , 4)

# variable  = (Element1, element 2,....element n)
# b = ( 1, 2, 3)
# print(type(b))

# # print(a)
# # a[1] = 6
# # print(a)

# #print(b)
# #b[1] = 6
# print(b[1])

#Dictonary Syntax
# variable = {}
# variable = {key 1 : vlue, key2: value, .... keyn : valuen}
# variable[key1] = value
# variable[keyn] = valuen
# a = {}
# a['name1'] = 'John'
# a['name2'] = 'Max'
# a['name3'] = 'Hari'

# print(a)
# print()
# print(a.items())

# for key in a.values():
#     print(key)


b = {}
b[1] = a
b[2] = 'Name'
print(b.items())




