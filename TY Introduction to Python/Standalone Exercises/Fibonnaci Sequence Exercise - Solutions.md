### Task 01
1. Set up 3 variables (Use unique names for all)
	1. Num1 = 0
	2. Num2 = 1
	3. Num3 = 0
2. Print Num1 and Num2 as the first 2 items in the sequence
3. Start a loop that runs  10 times
4. for each run of the the loop do
	1. Num3 = Num1 + Num2
	2. print Num3
	3. Num1 = Num2
	4. Num2 = Num3
### Task 02
```python
# Task 2 first 10 Items
Num1 = 0
Num2 = 1
Num3 = 0
print("The first item in the sequence will always be",Num1)
print("The next 10 items are:")
for i in range(10): #Will run the loop the amount of times in the range
	Num3 = Num1 + Num2 #Add the previous 2 numbers to form the next
	print(Num3)
	Num1 = Num2 #Moves Number 2 into the first position
	Num2 = Num3 #Moves Number 3 into the second position redy to find the next number in the sequence
```
### Task 03
```python
# Task 3 first 100 Items
Num1 = 0
Num2 = 1
Num3 = 0
print("The first item in the sequence will always be",Num1)
print("The next 100 items are:")
for i in range(100): #Will run the loop the amount of times in the range
	Num3 = Num1 + Num2 #Add the previous 2 numbers to form the next
	print(Num3)
	Num1 = Num2 #Moves Number 2 into the first position
	Num2 = Num3 #Moves Number 3 into the second position redy to find the next number in the sequence
```
### Task 04
```python
# Task 4 Ask How many Items
Num1 = 0
Num2 = 1
Num3 = 0
items = int(input("How many items in the sequence do you want to see? "))
print("The first item in the sequence will always be",Num1)
print("The next",items,"items are:")
for i in range(items): #Will run the loop the amount of times in the range
	Num3 = Num1 + Num2 #Add the previous 2 numbers to form the next
	print(Num3)
	Num1 = Num2 #Moves Number 2 into the first position
	Num2 = Num3 #Moves Number 3 into the second position redy to find the next number in the sequence
```
