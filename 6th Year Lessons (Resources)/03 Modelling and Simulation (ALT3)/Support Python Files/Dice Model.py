import random

def dice(userGuess):
    if userGuess == num:
        return True
    else:
        return False
    
num = random.randint(1,6)
#print(num)
userNum = int(input("Guess a number between 1 and 6: "))
result = dice(userNum)


if result:
    print("You are correct")
else:
    print("You are incorrect")