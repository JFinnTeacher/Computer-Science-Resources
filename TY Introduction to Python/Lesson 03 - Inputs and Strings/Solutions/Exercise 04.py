#Lesson 3 - Exercise 04
#Task 01 working with numbers
num1 = int(input("What is your first number "))
num2 = int(input("What is your Second number "))
floor_of_nums = num1 // num2
mod_of_nums = num1 % num2

print("The Floor of both numbers is", floor_of_nums)
print("The Modulus of both numbers is ", mod_of_nums)

# Taks 02 - Strings and numbers together
sentence = input("Type in a sentence ")
index = int(input("Type in a number smaller than the length of the sentence "))

print(sentence[index])
