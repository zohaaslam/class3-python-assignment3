# List in Python
# A bultin data type in Python that can be used to store a collection of items.
# It can store different types of items in a single list.
# List [] is a mutable data type.

# Example of List

list_name = ["Ali", "Jawwad", 43.3, "Present", 3 , 2 , 4]
print(list_name)

# Mutable data type
print(list_name[5])
list_name[1] = "Mohsin "
print(list_name)

names = ["zoha ","kainat","laiba","sana","saba"]
print(names)

students_data = ["Ali", 30.78, "jawad", 22.3 ]
print(students_data)
print(len(students_data))


# List Slicing:
# similar to string slicing
# list_name[start:end:step]
# start: starting index
# end: ending index

# Example of List Slicing

names_list = ["komal","jannat","miral","abrish","anabiya","alishba"]
print(names_list[0:5])
print(len(names_list))

num = [1,2,3,4,5,6,7,8,9,12,22,34,45,32]
print(num[3:8])
# print all elements from index 1 to end
print(num[1:])

# List Methods
# append() : add an element at the end of the list
# insert() : add an element at a specific index
# sort() : sort the list in ascending order
# reverse() : reverse the list

# append()
numbers = [1 , 2, 3]
numbers.append(7)
print(numbers)

# sort() ye none return karta hai
nums = [2,4,4,32,1]
print(nums.sort())

# sort(reverse=True) : sort the list in descending order

list = ["banana","apple","mango","grapse"]
list.sort(reverse=True)
print(list)

# reverse() : reverse the list
items = ["a","d","c","f","b","e"]
items.reverse()
print(items)

# insert() : add an element at a specific index
list = [2,1,3,4]
list.insert(3,5)
print(list)

# remove() : remove an element from the list
list_num = [22,11,33,44]
list_num.remove(11)
print(list_num)

# pop() : remove an element from the list at a specific index
lists_num = [23, 43, 32,23,33]
lists_num.pop(1)
print(lists_num)

# TUPLES IN PYTHON

tup  = (1,2,3,4,5,6,7)
print(tup)
print(tup[3])

tupl = ()
print(tupl)
print(type(tupl))

# Slicing In Tuples 
num = (1,2,3,4,5,6,7)
print(num[1:4])

num1 = (22,33,44,55,66,77,88,99,89,67)
print(num1[1:6])

# Tuple Methods
# index : return the index of the first element with the specified value

letters = ("a","b","c","d","e","f")
print(letters.index("e"))

num2 = (1,2,55,33,5)
print(num2.index(33))

# count 
num1 = (22,33, 33, 33, 33,44,55,66,77,88)
print(num1.count(33))

name = ("zoha","hina","hadiya","komal","zoha")
print(name.count("zoha"))