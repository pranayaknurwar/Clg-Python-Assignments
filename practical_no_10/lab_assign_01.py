"""
Create a Panda Dataframe script by reading a file "books.csv". The "books.csv" contains information regarding the books such as title, name of author, edition, publication year and publishing house, price. Create an application to perform the following operations:

a) Print the complete report of books in a Tabular form
b) Print the list of available books of a given author
c) Print the list of available books of a given publishing house
d) Print the Titles of cheapest & costliest book available
e) Print the list by sorting based on the year of publication
"""

import pandas as pd

df = pd.read_csv("books.csv")

print("Complete Book Report:")
print(df)

# b) Books by a given author
author_name = input("Enter author name: ")
print("\nBooks by", author_name)
print(df[df['author'] == author_name])

# c) Books by publishing house
publisher = input("\nEnter publisher name: ")
print("\nBooks by publisher:", publisher)
print(df[df['publisher'] == publisher])

# d) Cheapest and costliest books
print("\nCheapest Book:")
print(df[df['price'] == df['price'].min()])

print("\nCostliest Book:")
print(df[df['price'] == df['price'].max()])

# e) Sort by year
print("\nBooks sorted by year:")
print(df.sort_values(by='year'))