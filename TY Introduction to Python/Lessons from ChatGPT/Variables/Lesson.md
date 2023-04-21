# Lesson Title: Introduction to Variables in Python

**Objective: At the end of this lesson, the student should be able to:**

-   Define a variable in Python
-   Understand the rules for naming variables
-   Assign values to variables
-   Understand the concept of data types in Python

Introduction: In programming, variables are used to store values that can be used later in the program. In this lesson, we will learn about variables in Python and how to use them.

1.  Defining a Variable: A variable in Python is defined by assigning a value to it using the "=" operator. For example:
```python
x = 5
```
In this example, "x" is the variable name and "5" is the value assigned to it. The variable name can be any combination of letters, numbers, and underscores, but it cannot start with a number. It's recommended to use descriptive variable names to make the code more readable.

2.  Rules for Naming Variables: There are some rules that must be followed when naming variables in Python:

-   The name must start with a letter or underscore.
-   The name can contain letters, numbers, and underscores.
-   Variable names are case sensitive. For example, "x" and "X" are two different variables.
-   Variable names cannot be the same as Python keywords (such as "if", "else", "while", etc.).

3.  Assigning Values to Variables: Once a variable is defined, we can assign a value to it using the "=" operator. For example:
```python
x = 5
y = "Hello"
z = True
```
In this example, "x" is assigned the value 5, "y" is assigned the value "Hello", and "z" is assigned the value True. Note that variables can hold different types of values, such as integers, strings, and boolean values.

4.  Data Types in Python: In Python, every value has a data type. The most common data types are:

-   Integer (int): represents whole numbers, such as 1, 2, 3, etc.
-   Float: represents decimal numbers, such as 3.14, 2.5, etc.
-   String (str): represents text, such as "Hello", "World", etc.
-   Boolean (bool): represents True or False.

Python has built-in functions to determine the data type of a value, such as type():

```python
x = 5
y = "Hello"
z = True

print(type(x))    # Output: <class 'int'>
print(type(y))    # Output: <class 'str'>
print(type(z))    # Output: <class 'bool'>
```
Conclusion: Variables are an essential part of programming, and Python makes it easy to define, assign values, and manipulate them. In this lesson, we learned how to define variables, the rules for naming variables, assigning values to them, and the concept of data types in Python.