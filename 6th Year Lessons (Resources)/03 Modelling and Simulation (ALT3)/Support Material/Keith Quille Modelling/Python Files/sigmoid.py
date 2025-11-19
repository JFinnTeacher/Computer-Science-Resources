import math

def sigmoid(t):
    return  (1 / (1 + math.exp(-t)))

print(sigmoid(-10))


