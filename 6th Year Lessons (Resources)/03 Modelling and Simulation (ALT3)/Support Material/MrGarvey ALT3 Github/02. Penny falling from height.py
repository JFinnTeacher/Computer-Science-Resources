# Falling penny myth model

# You might have heard that a penny dropped from the top of the Empire State Building would be going so fast
# when it hit the pavement that it would be embedded in the concrete; or if it hit a person,
# it would break their skull.

# We can test this myth by making and analyzing a model

# If initial velocity of the penny is 0 m/s, then the time taken (t) for a penny to drop a height of (h) at acceleration (a) is
# t = square root(2h/a)
# Final velovity of the penny (v) is then calculated by : v=at

# Model 1 for fallin penny.
# Using Abstraction we ignore all factors that will affect the penny falling to find the velocity the penny was falling when it impacted with the floor or person.

import math

a = 9.8  # acceleration of gravity
h = 381  # Height of Empire state building

t=math.sqrt(2*h/a) # Find a value for time taken for object to fall
v=t*a              # Find the final velocity the object was travelling at at time of impact

print('This is our first iteration for modelling the velocity of a penny falling from the Empire state building,\nWe have ignored all external factors in this model')
print(f'\nA penny dropped from a height of {h}m will impact at a velocity of {round(v,2)}m/s')

# Could you change this model so the user selects a height from which an object is dropped?

# This iteration ignores air resistance, however, air resistance will affect the velocity at which the object travels so we can't truely say the velocity calculated
# on line 22 is the actually the final velocity of the penny upon impact.

# Model 2 ( Iteration 2)
# Using abstraction we will add relevant factors to our model, i.e the effect of wind resistance.
# Objects reach terminal velocity when the resistance of the medium through which it is falling prevents further acceleration, so the object then
# ends up travelling at a constant speed after a period of initial acceleration. In our second iteration of the model we will calculate the pennies terminal velocity

# Drag coefficients - https://en.wikipedia.org/wiki/Drag_coefficient ,See examples of drag coefficients here.
m=.0025 # Mass of a penny is 2.5g or .0025kg
g=9.8 # Gravity m/s2
p=1.225 # Density of fluid an object is falling through, air has a density of 1.225
A=.000285 # Area of object in contact with air resistance
C=1.15 # Drag coefficient of penny (the circular surface when falling)
Vt=math.sqrt((2*m*g)/(p*A*C))  # Vt is the terminal velocity

print('\nOur second iteration of the model includes air resistance to more accurately calculate the velocity of a falling penny')
print(f'\nIn our first model we calculated that a penny will fall at {round(v,2)}m/s from the Empire State Building')
print(f'In our second iteration, we included air resistance as a factor opposing the acceleration of our penny and found\nthe terminal velocity of a penny is {round(Vt,2)}')
print(f'\nThis means that when our pennt reaches {round(Vt,2)}m/s, it no longer accelerates so it will reach the floor travelling at {round(Vt,2)}m/s, significantly slower than {round(v,2)}m/s')

# Iteration 3,4.....etc
# How could you improve this program? Could you imporve the UI or the UX?
# Could you allow the user more control over the model by not hardcoding all the values?
# This model only works for a penny falling from the Empire State Building, what about other buildings?
# What about not using a penny and instead simulating a projectile such as a bullet?
# After how long in freefall does the penny reach terminal velocity?
# The units used here are m/s, what about km/hr or miles/hr?