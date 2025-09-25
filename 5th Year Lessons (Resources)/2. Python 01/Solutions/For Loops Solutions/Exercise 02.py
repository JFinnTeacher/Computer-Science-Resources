'''
Exercise 02
Summing numbers 1 to 100
'''

total = 0 # Initialise the variable. Ensures it is created and empty ready for use

for number in range(1,100+1): #The variable can be called anything you want
    total = total + number # This adds the number to the current value of total and then places that into the total replacing the previous value
    
print("The total of adding the numbers 1 to 100 is ",total)