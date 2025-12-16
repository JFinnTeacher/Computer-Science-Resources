'''
Title: ALT2 Project using Database of Astronaut Information using Pandas
Author: J Finn
Date: Dec 2025
'''

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
# Load the CSV File 
df = pd.read_csv('astrodbase.csv')

# Process the data to extract information of time spent in space by country
def convert_to_hours(time_space):
    parts = time_space.split(":")
    total_hours = (int(parts[0])*24) + int(parts[1])
    return total_hours

df['Total Hours'] = df['Total Flight Time (ddd:hh:mm)'].apply(convert_to_hours)

# Show Visualization of time spent in space by country
print(df.groupby('Country')['Total Hours'].sum().sort_values(ascending=False))

plt.pie(time_in_space, labels=unique_countries, autopct='%1.0f%%', 
        textprops={'fontsize': 8})
# Process the data to extract the information by gender

# Show Visualization of time spent in space by gender

