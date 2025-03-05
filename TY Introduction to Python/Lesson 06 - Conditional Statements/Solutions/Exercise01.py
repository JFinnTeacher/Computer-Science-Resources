# Lesson 06 - Exercise 01
# Task 01
age = int(input("What is your age? "))

if age >= 18:
  print("You are eligable to vote")
else:
  print("You are no eligable to vote")

# Task 02
length = int(input("What is the length of the shape? "))
width = int(input("What is the width of the shape? "))

if length == width:
  print("This is a square as the 2 sides are the same length")
else:
  print("This is not a square as the 2 sides are different lengths")

#Task 03
num1 = int(input("What is your first numnber? "))
num2 = int(input("What is your second number? "))

if num1 > num2:
  print("The first number ",num1," is larger than the second number")
else:
  print("The Second Number ",num2," is larger than the first number")