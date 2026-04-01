"""   
            carat        cut        color      clarity       depth       table  price    x     y     z
0            0.23        Ideal       E           SI2          61.5        55.0   326    3.95  3.98  2.43
1            0.21        Premium     E           SI1          59.8        61.0   326    3.89  3.84  2.31
2            0.23        Good        E           VS1          56.9        65.0   327    4.05  4.07  2.31
3            0.29        Premium     I           VS2          62.4        58.0   334    4.20  4.23  2.63
4            0.31        Good        J           SI2          63.3        58.0   335    4.34  4.35  2.75

Do following:

i) Calculate the mean of price for each cut of diamonds DataFrame given above.
ii) Print count of diamond, minimum price and maximum price for each cut of diamonds in above given DataFrame.
iii) Calculate and print average value of parameter x, y, and z separately.

"""

import pandas as pd

# Create DataFrame
data = {
    'carat': [0.23, 0.21, 0.23, 0.29, 0.31],
    'cut': ['Ideal', 'Premium', 'Good', 'Premium', 'Good'],
    'color': ['E', 'E', 'E', 'I', 'J'],
    'clarity': ['SI2', 'SI1', 'VS1', 'VS2', 'SI2'],
    'depth': [61.5, 59.8, 56.9, 62.4, 63.3],
    'table': [55.0, 61.0, 65.0, 58.0, 58.0],
    'price': [326, 326, 327, 334, 335],
    'x': [3.95, 3.89, 4.05, 4.20, 4.34],
    'y': [3.98, 3.84, 4.07, 4.23, 4.35],
    'z': [2.43, 2.31, 2.31, 2.63, 2.75]
}

df = pd.DataFrame(data)

print("DataFrame:\n", df)

# i) Mean price for each cut
print("\nMean price for each cut:")
print(df.groupby('cut')['price'].mean())

# ii) Count, min, max price for each cut
print("\nCount, Min, Max price for each cut:")
print(df.groupby('cut')['price'].agg(['count', 'min', 'max']))

# iii) Average of x, y, z
print("\nAverage values of x, y, z:")
print(df[['x', 'y', 'z']].mean())