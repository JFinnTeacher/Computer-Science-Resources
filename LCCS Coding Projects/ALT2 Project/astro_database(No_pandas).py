'''
Title: ALT2 Project using Database of Astronaut Information without using Pandas
Author: J Finn
Date: Dec 2025
'''

# Import necessary libraries
import csv
import matplotlib.pyplot as plt
import os

# Initilise the required lists for processing
names = []
countries = []
genders = []
flights = []
total_flights = []
flight_times = []

# Load the CSV File 
with open(os.path.join(os.path.dirname(__file__), "astrodbase.csv"), "r", newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header
    
    for row in csv_reader: # append row[0] to names etc
        names.append(row[0])
        countries.append(row[1])
        genders.append(row[2])
        flights.append(row[3])
        total_flights.append(row[4])
        
        # Flight times in the form of day,hours,mins This needs to be converted to
        # a single value of hours
        time_parts = row[5].split(":")
        days = int(time_parts[0])
        hours = int(time_parts[1])
        mins = int(time_parts[2])
        total_hours = ((days*24) + hours)
        
        #add the calculated value to flight times variable
        flight_times.append(total_hours)

# Process the data to extract information of time spent in space by country
# Start by creating 2 lists - 1 to record the countries and 1 to store the time in space.
# If the code finds a country that is not on the list then add that country and add the hours

unique_countries = []
time_in_space =[]
location = 0

for i in range (len(countries)):
    country = countries[i]
    hours = flight_times[i]
    
    # Is country already on the list
    if country in unique_countries:
        location = unique_countries.index(country)
        time_in_space[location] = time_in_space[location] + hours
    else:
        unique_countries.append(country)
        time_in_space.append(hours)

#sort the lists in decending order

for i in range(len(time_in_space)):
    #find the position of the maximum time in space
    max_position = i
    for j in range(i +1, len(time_in_space)):
        #Check if the current value is larger than the maximum value
        if time_in_space[j] > time_in_space[max_position]:
            max_position = j #Sets the position to the maximum value
            
    # Move the time in space value to the current max value
    temp = time_in_space[i]
    time_in_space[i] = time_in_space[max_position]
    time_in_space[max_position] = temp
        
    #Swap the countries using the same values
    temp = unique_countries[i]
    unique_countries[i] = unique_countries[max_position]
    unique_countries[max_position] = temp


# Show Visualization of time spent in space by country

plt.pie(time_in_space, labels=unique_countries, autopct='%1.0f%%', 
        textprops={'fontsize': 8})

# Process the data to extract the information by gender
unique_gender = []
time_in_space =[]
location = 0

for i in range (len(genders)):
    gender = genders[i]
    hours = flight_times[i]
    
    # Is country already on the list
    if gender in unique_gender:
        location = unique_gender.index(gender)
        time_in_space[location] = time_in_space[location] + hours
    else:
        unique_gender.append(gender)
        time_in_space.append(hours)
# Show Visualization of time spent in space by gender
plt.figure(figsize=(8, 8))
plt.pie(time_in_space, labels=unique_gender, autopct='%1.1f%%')
plt.title("Total Time in Space by Gender")
plt.show()
    
