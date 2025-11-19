'''
Exercise 04
Times Tables
'''
# Get user input
num=int(input('Please enter a positive integer between 1 and 15: '))

for i in range(1, 12+1):
    print(num, " x ", i, " = ", num*i)
# Display the times table for the number entered