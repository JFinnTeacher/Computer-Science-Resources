# Lesson 03 - Inputs and Strings

## Exercise 01

### Task 1

Take in a string variable for your name from the user. Do this by using the input() function.

```python
name = input()
```

it is up to you if you want to prompt the user for input or leave the input function blank.

### Task 2

Add to task 1 by adding a print function to your program and printing out the name variable.

### Task 3

Copy and paste the code from the code section into repl.it.

Use string indexing to print out the letter “m” in the string “Salamander”.

| S    | A    | L    | A    | M    | A    | N    | D    | E    | R    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    |

Code:

```python
reptile = "Salamander"
print(reptile[]) 
```

### Task 4

Copy and paste the code from the code section into repl.it.

Use string slicing to print out the first two characters in the string “Whale”.

| W    | H    | A    | L    | E    |
| ---- | ---- | ---- | ---- | ---- |
| 0    | 1    | 2    | 3    | 4    |

Code:

```python
mammal = "Whale"
print(mammal[:]) 
```

## Exercise 02

### Task 1

Using the input function, take in your first and last name as the variables:

```
first_name, last_name.
```

Concatenate (add together) the 2 variables and assign them to the variable: full_name.

*Hint* Remember to add in a blank space between the 2 names.

Use the print() function to display the full name variable to your screen.

### Task 2

Using the input() function, take in your age as an integer variable, call the variable:

```
 my_age
```

print out the age variable using the print() function.

### Task 3

Copy the String variable: biggest_animal = "blue whale" into repl.it and use string slicing to print out the first and last character of the string.

Code:

```
biggest_animal = "blue whale" 
```

### Task 4

Using the input function, take in 2 numbers as the variables: num_1 and num_2

Multiply the 2 numbers and assign them to a variable called: answer

Print out the answer variable.

## Exercise 03

### Task 1

You are going to use string slicing to find the 2 hidden animals inside my_word.

I will start you off with most of the code, see if you can find the 2 hidden animals inside this word.

```
my_word = "cupboard"
print(my_word[3:])
print(my_word[3:])
```

### Task 2

Using the input() function take in values for the variables:

·    Name

·    Age [remember this will be an integer “int()” but a string when printing it out “str()”]

·    Address

·    Number (You can leave your number as a string)

Use either String concatenation (adding together) or formatting “format()” to output the sentence:

Hello name you are age years old, you live at address and your phone number is number.

### Task 3

Using string slicing, slice the first 3 characters from the first_word and second_word variables.

Assign each new 3 letter word to the variables: start_of_new_word, end_of_new_word. Concatenate the 2 new 3 letter Strings to make an entirely new word and then print the new word.

```python
first_word = "barbeque"
second_word = "relative"

start_of_new_word = first_word[:]
end_of_new_word = second_word[:]
new_word = start_of_new_word + end_of_new_word
print(new_word)
```

## Exercise 04

### Task 1

A You are tasked with taking in 2 numbers from the user.

You will floor and mod the first number by the second number.

Assign the floor to a new variable called: floor_of_nums

Assign the mod to a new variable called: mod_of_nums

Print out the 2 variables.

*Hint* If you cannot remember the floor and mod operators

- Floor is like standard Division but discards any remainder and is carried out using //
- Mod or Modulus is standard division but only returns the remainder and is carried out using %

### Task 2

You will be taking in both a string and a number from the user using the input() function.

You are going to use the number as the index of the string to print out a certain character.

The number you take in from the user must be a valid index within your String. Remember that indexing starts at 0!
