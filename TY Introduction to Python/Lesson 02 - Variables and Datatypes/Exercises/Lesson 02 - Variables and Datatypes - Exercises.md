# Lesson 02 - Variables and Datatypes Exercises

## Exercise 01
### Task 1:
We are going to experiment with variables by creating a mad libs game.
A mad libs game uses a story as a template and allows you to choose what words you wish to use by using variables in certain places which can be replaced.

**How does it work?**
Just copy and paste the code below into your code editor. 
You can do this by highlighting the code section and using either right click and copy or
Highlighting the code section and pressing *ctrl+c* on your keyboard.
Then navigate to your code editor and hold *ctrl + v* to paste the code into the code editor.

**Now we have the code in the code editor**
After each variable name, in between the "" you can put in your own words! So, if your name is Amanda and your favourite food is Sushi, you would put:
your_name = "Amanda"
your_favourite_food = "Sushi"
And so on until you have chosen words for each variable. You can change the words in between the "" as many times as you like to get a new story each time!

```python
your_name = "" 
your_favourite_food = ""
something_youre_good_at = ""
something_you_are = ""
embarrassing_thing_you_did = ""
nice_thing_you_do = "" 

print("Face it, " + your_name + ", you are about the greatest\nthing since " + your_favourite_food + ". No one else can " + something_youre_good_at + "\nlike you can. Your best friend says you are\nthe " + something_you_are + "-est person in the world! Sure, you\nonce " + embarrassing_thing_you_did + ", but you also " + nice_thing_you_do + " so\nreally, you are the best”)
```
## Exercise 02

### Task 1:
Declare and assign a variable for your surname.
**Recall, we do need quotation marks when assigning strings and characters to variables.**
Use the print function to print out the variable.
### Task 2:
Declare and assign a variable for your birth year.
**Recall, we don’t need quotation marks when assigning integer(whole) numbers to variables.**
Use the print function to print out the variable.

### Task 3:
Replace the ? With the correct operator to replicate the output given.

```python
print(10 ? 5)
Expected Output: 15
print(10 ? 5)
Expected Output: 5
print(10 ? 5)
Expected Output: 50
print(10 ? 5)
Expected Output: 2
```


## Exercise 03

### Task 1:
You can concatenate (add together) strings and variables using the + operator.
For example:
```python
name = "Sally"
age = "sixteen" 
print("Hi " + name + ", you are " + age + " years old.")
```

 Outputs: 
```
Hi Sally, you are sixteen  years old.   
```

Copy the variable declarations and print statement into your code editor and make sure it runs. 
Modify the print statement to output:

```
Hi *name*, you are *age* years old and you live in *town*. You travel to school by *use*. 
```
You will need to create a new variables for town and use values that make sense for you.

### Task 2:
Write 2 different Python statements that each add 1 to the integer variable x, which has the value 10.
You can do this in your code editor and print out the result or feel free to use pen and paper.
*Hint* remember our assignment operator table!

### Task 3:
Create two variables, one named **house_width** and another named **house_length**
Use these variables in **a print function** to find the perimeter (length*2 + width*2) of a house with:

A)
A length of 14m
A width of 8m
B)
A length of 18m
A width of 12m

Remember, for the second calculation, you only need to change the values contained in the variable.

## Exercise 04
### Task 1:
A house sits on a plot of land that has the area: 20 * 15
The house itself has the area: 15 * 10
Calculate the area of the land and store this value in a variable: area_of_land
Calculate the area of the house and store this value in a variable: area_of_house
Calculate the area of the garden and store this value in a variable: area_of_garden
To get the area of the garden, you need to minus area_of_house from the area_of_land
Print the area of the garden using a print() function in this format:
print("The area of the garden is", area_of_garden, "m2")
**When we want to add integer values into a print function that already contains a string, we use a comma (,) instead of a plus (+)**

### Task 2:
Using variables for:
*pi
radius*

Calculate the area of a circle using Python and store the result in a variable called area_of_circle. Then print out the area_of_circle variable.
The formula for calculating the area of a circle is: πr<sup>2</sup>
The variable: pi should be set to: 3.14159
The variable: radius can be set to whatever you choose but be sure to check your answers!

> [!HINT]
> When doing the r<sup>2</sup> remember ** is for Exponentiation OR (r * r) is also fine in this case.
> Remember to use PEMDAS in the calculation! 
> Sample ans: When pi is set to 3.14159 and radius is set to 7. The area of the circle is 153.93791.

 

 

 