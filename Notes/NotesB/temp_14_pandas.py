# Pandas
import pandas as pd
import random

d = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}

df = pd.DataFrame(data=d)
print(df)
print(df['col1'])
print(df.describe())

# lists > dicts > series/dataframes

# Pandas series (1d array)
s = [random.randrange(100) for x in range(10)]
my_series = pd.Series(s)
print(my_series)

# Pandas DataFrame (2d spreadsheet (kinda))
# make from dict
d = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data=d)
print(df)

# could also maike it from a list/array
d = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
cols = ["A", "B", "C"]
df2 = pd.DataFrame(data=d, columns=cols)
print(df2)

# make a df from a csv
df3 = pd.read_csv("import_me/Parks_-_Public_Art.csv")
print(type(df3))

# handy methonds
print(df3.head()) # first 5 rows in df
print(df3.tail(10))
print(df3.info())
print(df3.describe()) # basic stats

# useful attributes
print(df3.index) # theses are the rows (data key)
print(df3.columns) # index object
print(df3.dtypes) # data types

# simple selection using []
art = df3['ART'] # index kinda like dictionary
print(type(art))

# we can also slice the df using .iloc[] (index location)
first5_parknames = df3.iloc[:5, 0] # rows, cols
print(first5_parknames)

first_fifth_artists = df3.iloc[[0, 4], [2, 3]]
print(first_fifth_artists)
print(type(first_fifth_artists))




