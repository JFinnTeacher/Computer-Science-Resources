#Code Resource - https://tinyurl.com/4wv2d32y
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from sklearn.linear_model import LinearRegression
'''
data =\
[
[2010, 445],
[2011, 439],
[2012, 297],
[2013, 264],
[2014, 245],
[2015, 246],
[2016, 191],
[2017, 180],
[2018, 201],
[2019, 162],
[2020, 195],
[2021, 132],
]

data =\
[
[1,1],
[2,3],
[3,5],
[4,7],
[5,9],
[6,11]
]

'''
#You can use panda's to read this data from a file like this:
csv = pd.read_csv('Pirates.csv')

#select your data columns
data = csv[['Year', 'Pirates']]

#Lets you say which will be x and y
x = data['Year']
y = data['Pirates']

x = np.array(data)[:,0].reshape(-1,1)
y = np.array(data)[:,1].reshape(-1,1)
print("X=")
print(x)
print("y=")
print(y)

to_predict_x= [2022,2023,2024]
to_predict_x= np.array(to_predict_x).reshape(-1,1)

regsr=LinearRegression()
regsr.fit(x,y)

predicted_y= regsr.predict(to_predict_x)
m= regsr.coef_
c= regsr.intercept_
print("Predicted y:\n",predicted_y)
print("slope (m): ",m)
print("y-intercept (c): ",c)

plt.title('Pirate Attacks: Predict the next years')  
plt.xlabel('Years')  
plt.ylabel('Attacks') 
plt.scatter(x,y,color="blue")
new_y=[ m*i+c for i in np.append(x,to_predict_x)]
new_y=np.array(new_y).reshape(-1,1)
plt.plot(np.append(x,to_predict_x),new_y,color="red")
plt.show()
