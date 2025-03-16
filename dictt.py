# Dictionary in Python
#  A builtin data type in Python . It used to store data values in key:value pairs.
# They are unordered, changeable and does not allow duplicate values.

info = {
    "name": "zoha",
    "age": 19,
    "subject" : ["Python","Java","Html","Css","typescript"],
    "topics": ("dictionary","sets"),
    "marks": 89.9,
    "is_adult" : True,
    "learning": "pyton"
}

print(type(info))
print(info["learning"])

# assign a new value
info["name"] = "Abrish"
info["age"] = 15
print(info)

# create  a null dictionary 
null_dict = {}
print(null_dict)
# values assign in null dictionary
null_dict["name"] = "Arham"
print(null_dict)


# Nested Dictionary

student_info = {
    "name": "Haniya",
    "roll no": 22,
    "age": 14,
    "subjects" : {
        "maths" : 70,
        "chem" : 89,
        "phy" : 66,

    }
}
print(student_info)
print(student_info["subjects"])
print(student_info["subjects"]["maths"])


# Dictionary Methods
# key() returns all keys nested wali ni ati isme.


student_info = {
    "name": "Haniya",
    "roll no": 22,
    "age": 14,
    "subjects" : {
        "maths" : 70,
        "chem" : 89,
        "phy" : 66,

    }
}

print(student_info.keys())

# type cast
print(list(student_info.keys()))

# values() : returns all values

student_info = {
    "name": "Haniya",
    "roll no": 22,
    "age": 14,
    "subjects" : {
        "maths" : 70,
        "chem" : 89,
        "phy" : 66,

    }
}
print(student_info.values())


# items() : returns all key value pairs
student_info = {
    "name": "Haniya",
    "roll no": 22,
    "age": 14,
    "subjects" : {
        "maths" : 70,
        "chem" : 89,
        "phy" : 66,

    }
}
print(student_info.items())

# .get return the key according to value

student_info = {
    "name": "Haniya",
    "roll no": 22,
    "age": 14,
    "subjects" : {
        "maths" : 70,
        "chem" : 89,
        "phy" : 66,

    }
}
print(student_info["age"])  
print(student_info.get('age'))

# print(student_info["age2"])  # error  
print(student_info.get('age2'))  # return None

# update(new dict) insert the specified items in dictionary 
student_info = {
    "name": "Haniya",
    "roll no": 22,
    "age": 14,
    "subject": "english",
}
print(student_info.update({"city":"karachi","religion":"Islam"}))
print(student_info)
# way 2
new_dict = {"gender": "female"}
student_info.update(new_dict)
print(student_info)


# Set in Python 
# Set is the collection of the unorderd items. isme koi bhi index ni hota koi bhi values phly askti hen
# Each elements in the set must be unique and immutable 

num = {1,2,3,4,5,6,7,8}
print(num)
print(type(num))

collection = {"zoha" , 1, 3, 5 ,6 , True, 45.6, "right"}
print(collection)


num2 = {1,2,2,3,3,3,}
print(num2)

# Empty Set 
empty_set = {}  # wrong way
empty_set1 = set()  # right way
print(empty_set1)

# Set Methods  sets mutable hota h but set k elemenst immutable hote hen 
# add add an element

num2 = {1,2,2,3,3,3,}
num2.add(44)
num2.add(89)
print(num2)


# remove() removes the elemsts an

num2 = {1,2,2,3,3,3,}
num2.remove(3)
num2.remove(1)
print(num2)


# clear() empiest the set

num2 = {1,2,2,3,3,3,}
num2.clear()
print(num2)


# pop() removes a random value

num2 = {1,2,2,3,3,3,4,5,6,7,8}

print(num2.pop())

