# Million Dice Roll Statistics sim

import random       # Import modules needed for code

print('This sim will model the statistics of 1 million dice rolls for a used defined number of dice')    # Telling user what program does
numberofDicetoRoll=int(input('Please enter how many dice you want to roll: '))    # Ask user for their input

dieRoll=[0]*(numberofDicetoRoll*6+1)   # Create a blank list for possible numbers
results=[0]*(numberofDicetoRoll*6+1)   # Create a blank list for results

# Setting the count of the sum of the three dice rolled to 0
for i in range(numberofDicetoRoll,(numberofDicetoRoll*6)+1):   # Setting out the largest and smallest numbers that can be made when the dice are rolled. 
    dieRoll[i]=i+1 # e.g if you set numberofDicetoRoll to 3, then the smallest value that can be rolled is 3 (1 on each dice), whereas the biggest can be 18 (6 on each dice)
    results[i]=0
    
print(f'Simulating 1,000,000 rolls of {numberofDicetoRoll} dice...')

for i in range(1000000):  # Loop that runs the dice rolling 1 million times
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