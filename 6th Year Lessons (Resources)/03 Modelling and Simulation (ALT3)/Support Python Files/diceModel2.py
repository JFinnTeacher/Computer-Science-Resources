import random

def dice():
    return random.randint(1,6)

count = 0
userGuess = 3

for i in range(600):
    result = dice()
    print(result)
    
    if userGuess == result:
        count = count + 1

print("Count:" ,count)