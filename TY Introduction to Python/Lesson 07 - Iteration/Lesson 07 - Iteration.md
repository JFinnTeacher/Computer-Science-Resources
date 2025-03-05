# Lesson 06 Exercises – Iteration

## Exercises 01

### Task 1:

Using a while loop, write a program which will print the numbers from 1 to 10 on the screen.

### Task 2:

Using a while loop, write a program which will print the numbers from 10 to 1 on the screen

### Task 3:

If the following piece of code prints all the odd letters of a string, modify it to print all the even values of a string

```python
inputString = input("Please enter a string: ")
counter = 0

while counter < len(inputString):
    if counter % 2 == 0:
        print(inputString[counter])
	counter += 1
```

### Task 4:

Create a graphical user interface (GUI) using the print function for the previous tasks to be presented for the end user. And test their functionality with the GUI. Use the example below as a reference.

```
══════════════════════════════════════

  *   Graphical User Interface   *

══════════════════════════════════════

 1-  Print numbers from 1 to 10
 2-  Print numbers from 10 to 1
 3-  Find even values of a string
 4-  Exit

══════════════════════════════════════

Enter your choice from the menu:   
```

*Hint* Remember to put the user input for the menu after each choice to break the loop.



## Exercise 02

### Task 1:

Write a program using a for loop to print all numbers between 1 and 100 on the screen.

### Task 2:

Write a program using a for loop to print all odd numbers between 1 and 100 on the screen.

### Task 3:

Using a while loop, write a program which will ask to user to constantly accept names of students from the user. When the user is ready to stop, the loop should end when the keyword “stop” is entered.

## Exercise 03

### Task 1:

Write a program which takes in 10 integers from keyboard using a for loop and print their average value on the screen.

### Task 2:

Write a program, which will accept a single digit from the keyboard. Print out the multiplication tables for that number.

### Task 3:

Copy the following code and modify it to sum up the numbers and print their average.

```python
inNumber = int(input("Please enter a number: "))
while inNumber != "stop":
    print("Number added was :", inNumber)
    inNumber = input("Please enter another number:")
    if inNumber.isnumeric():
        inNumber = int(inNumber)                                
```

 

 

 

 