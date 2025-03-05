#Lesson 03 - Exercise 03
#Task 01 - Slicing Strings
my_word = "cupboard"
print(my_word[3:7])
print(my_word[3:6])

#Task 02 - Mixing Strings and Integers with Concatentation
name = input("What is your name ")
age = int(input("what is your age "))
address = input("Where do you live ")
number = str(input("What is your phone number "))

output = "Hello " + name + " you are " + str(age) + " Years old, You live in " + address + " and your phone number is " + number
print(output)

#Task 03 - Slicing Strings
first_word = "barbeque"
second_word = "relative"

start_of_new_word = first_word[0:3]
end_of_new_word = second_word[5:8]
new_word = start_of_new_word + end_of_new_word
print(new_word)