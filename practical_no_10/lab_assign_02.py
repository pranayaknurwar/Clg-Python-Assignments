"""
Create a table showing information about 5 states such as:

a) Name of the state
b) Area
c) Population

Generate the following reports:

a) Print the complete information of states
b) Print the name of the State having largest Area
c) Print the name of State having largest population
d) Create a mechanism to calculate the population density of States
e) Determine the name of State with highest population density
"""

import pandas as pd

# Create data
data = {
    'State': ['Maharashtra', 'Gujarat', 'Karnataka', 'Rajasthan', 'Punjab'],
    'Area': [307713, 196244, 191791, 342239, 50362],
    'Population': [112374333, 60439692, 61095297, 68548437, 27743338]
}

df = pd.DataFrame(data)

# a) Print complete info
print("State Information:")
print(df)

# b) State with largest area
print("\nState with Largest Area:")
print(df[df['Area'] == df['Area'].max()]['State'])

# c) State with largest population
print("\nState with Largest Population:")
print(df[df['Population'] == df['Population'].max()]['State'])

# d) Calculate population density
df['Density'] = df['Population'] / df['Area']

print("\nPopulation Density:")
print(df[['State', 'Density']])

# e) State with highest density
print("\nState with Highest Population Density:")
print(df[df['Density'] == df['Density'].max()]['State'])