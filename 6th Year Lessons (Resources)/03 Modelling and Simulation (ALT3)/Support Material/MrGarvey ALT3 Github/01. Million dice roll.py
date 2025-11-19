# Million Dice Roll Statistics sim

import random, time       # Import modules needed for code

print('This sim will model the statistics of 1 million dice rolls for a used defined number of dice')    # Telling user what program does
numberofDicetoRoll=int(input('Please enter how many dice you want to roll: '))    # Ask user for their input

results={}   # Create a blank dictionary

# Setting the count of the sum of the three dice rolled to 0
for i in range(numberofDicetoRoll,(numberofDicetoRoll*6)+1):   # Setting out the largest and smallest numbers that can be made when the dice are rolled. 
    results[i]=0                                               # e.g if you set numberofDicetoRoll to 3, then the smallest value that can be rolled is 3 (1 on each dice), whereas the biggest can be 18 (6 on each dice)
    
print(f'Simulating 1,000,000 rolls of {numberofDicetoRoll} dice...')

# % completed dislay
lastPrintTime = time.time() # Current time in seconds
for i in range(10):   # 1 millions iterations
    if time.time() > lastPrintTime + 1:    # If current time in seconds is greater than another time then display %, +1 is just a value plucked from the air, it could be anything
        print('{}% done...'.format(round(i / 10000, 1)))   # Display a % value
        lastPrintTime = time.time()                        # Change the value assigned to the variable lastPrintTime
   
   # Nested loop that counts how often each number appears
    total = 0 # total gets reset to 0 before the loop runs
    for j in range(numberofDicetoRoll):       # Run the for loop 
        total = total + random.randint(1, 6)  # Getting the sum of each dice roll
    results[total] = results[total] + 1       # 

# Display results:
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(numberofDicetoRoll, (numberofDicetoRoll * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print('  {} - {} rolls - {}%'.format(i, roll, percentage))