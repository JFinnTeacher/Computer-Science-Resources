# Lesson 06 - Exercise 03
#Task 01
age1 = int(input("What is the first age? "))
age2 = int(input("What is the Second age? "))
age3 = int(input("What is the third age? "))

if age1 > age2 and age1 > age3:
    print("Person 1 is the oldest")
elif age2 > age1 and age2 > age3:
    print("Person 2 is the oldest")
else:
    print("Person 3 is the oldest")

if age1 < age2 and age1 < age3:
    print("and Person 1 is the youngest")
elif age2 < age1 and age2 < age3:
    print("and Person 2 is the youngest")
else:
    print("and Person 3 is the youngest")


# Task 02
checkodd = int(input("Please enter a number to check for odd "))

remain = checkodd % 2

if remain == 0:
    print("The number you entered is an even number")
else:
    print("The number you entered is odd")


