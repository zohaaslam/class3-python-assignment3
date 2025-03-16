# Class 3 Assignment 3 

# Conditional Statements (if , elif , else)

name : str = "green"
if (name == "red"):
    print("stop")
elif(name == "green"):
    print("go")
elif(name == "yellow"):
    print("wait")

# ================================

num : int = 20

if (num == 32):
    print("You are not eligible for admission")
elif(num >= 18):
    print("You are eligible for admission")

# =================================

age : int = 18
if (age >= 25):
    print("You are eligible to vote")
elif (age == 10):
    print("You are not eligible to vote")
elif(age == 18):
    print("You can vote.")

# =================================

religion : str = "Muslim"
if(religion == "Hindu"):
    print("You can't eat beef")
elif(religion == "chiristian"):
    print("You can eat beef")
elif(religion == "Muslim"):
    print("You can eat beef")

# =================================

drink : str = "Pakola"
if(drink == "Pepsi"):
    print("You can drink Pepsi")
elif(drink == "Coke"):
    print("You can drink Coke")
else:
    print("Pakola is not available.")

# ====================================

marks = 95

if(marks >= 90 and marks >= 90):
    print("You have passed the exam with A grade")
elif(marks >= 80 and marks < 90):
    print("You have passed the exam with B grade")
elif(marks >= 70 and marks < 80) :
    print("You have passed the exam with C grade") 
else:
    print("You have failed the exam")     

# ==================================== 
# Nesting 
age = 30

if(age >= 40):
    if(age >= 45):
        print("You can go for studying abroad")
    else:
        print("You cant go")
else:
    print("you cant go")        

# =====================================

date = 17
if(date != 17):
    print("Your Birthday is coming soon!")
if(date >= 20):
        print("You are getting older")
else:
        print("Today is your Birthday")


# ==========================================
season_name = "summer"
if(season_name == "autumn"):
    print("Its's autumn season")
if(season_name == "winter"):
        print("It's winter season")
if(season_name == "summer"):
         print("It's summer season")
else:
            print("It's spring season")
 # ====================================

#  Even and Odd numbers
num = int(input("Enter a Number:"))
if(num % 2 == 0):
     print("The number is even")
else:
     print("The number is odd")

 #  ====================================
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
if(a > b and a > c):
     print("A is greater")
elif(b > c):
     print("B is greater")
else:
     print("C is greater")

 # ====================================

#  divide_num = int(input("Enter a Number:"))

# if(divide_num % 7 == 0):
#     print("The number is divisible by 7")
# else:
#     print("The number is not divisible by 7")        