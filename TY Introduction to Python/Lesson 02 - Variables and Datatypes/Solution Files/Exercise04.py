#Lesson 02 Samples - Exercise 04 - More Complex Calculations
#Task 01 - Calculating area of rectangle
#Assign the Variables needed
length_plot = 20
width_plot = 15
length_house = 15
width_house = 10

#Operations to calculate the various areas and store these in variables
area_plot = length_plot*width_plot
area_house = length_house*width_house
area_garden = area_plot - area_house

#Output the final value for the size of the Garden. Note the use of commas outside " " to seperate the number from the string.
# This tells the print command that you are switching from string to something else.
print("The Area of the Garden is ", area_garden, "m2")

#Task 02 - Calculating Area of Circle
#Assigning variables needed
pi = 3.14159
radius = 7
#Area of circle is pi times the radius squared. use PEMDAS to ensure it is carried out in the correct order
area_of_circle = (pi*(radius**2)) #** is to create the exponent

#printing out the final value
print("The area of the circle with Radius ",radius," is ",area_of_circle,"m2")
