#csv file source: https://www.statista.com/statistics/266292/number-of-pirate-attacks-worldwide-since-2006/

#calc the trendline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



csv = pd.read_csv('Pirates.csv')

#select your data columns
data = csv[['Pirates', 'Year']]

#Lets you say which will be x and y
x = data['Pirates']
y = data['Year']

print(x)
#choose your graph type
plt.scatter(x, y)

#some maths
z = np.polyfit(x, y, 1) #1 is linear, 2 is quadratic, 3 is cubic (polynomial fun!)
f = np.poly1d(z) #1d is a line. There's no 2d because you can't have a 2d line, that's a square.
plt.plot(x,f(x),"r--") #plot

#z returns two values in a list eg. [-3.91792431e-05  1.56428161e+01]
#The first value z[0] is the slope and the second x[1] is the y intercept
print("z will give you ", z)


print("The slope is", z[0])
print("The intercept is", z[1])

#here we can round off things to 2 digits so that the equation isn't too ugly and long
#This is the equation of a line    y=        m             x    +    c
print("The equation of the line is y="+str(round(z[0],2))+"x+"+str(round(z[1],2)))

#shows your graph in a new window
plt.show()

