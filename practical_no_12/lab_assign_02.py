"""
Create a program that reads "employee.xlsx" file of Infosys Software Solutions which includes columns such as Employee ID, Employee Name, Department, Designation etc.

Construct a program to print the following reports:

a) Print the list of employees working for "Automotive" domain.
b) Print the details of an employee with employee ID given by an end user.
c) Print the list of all the Developers of Infosys.
"""

import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

print("Employee Data:\n", df)

# a) Employees in Automotive domain
print("\nEmployees in Automotive Domain:")
print(df[df['Department'] == 'Automotive'])

# b) Search by Employee ID
emp_id = int(input("\nEnter Employee ID: "))
print("\nEmployee Details:")
print(df[df['Employee ID'] == emp_id])

# c) List of Developers
print("\nList of Developers:")
print(df[df['Designation'] == 'Developer'])