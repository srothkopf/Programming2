'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately


1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
2  Plot bus usage for the same years as a second line on your graph. (5pts)
3  Plot total usage on a third line on your graph. (5pts)
4  Add a title and label your axes. (4pts)
5  Add a legend to show data represented by each of the three lines. (4pts)
6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
'''

import matplotlib.pyplot as plt
import csv

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)

headers = data.pop(0)
print(headers)

recent_data = data[-11:]

ridership = [x[-1] for x in data]

trains = [int(x[3]) for x in recent_data]
busses = [int(x[1]) for x in recent_data]

total = [int(x[-1]) for x in recent_data]

plt.figure(1, tight_layout=True)
year_numbers = [x for x in range(11)]
year_names = [x[0] for x in recent_data]

plt.plot(year_numbers, total, color='purple', label='Total Riders')
plt.plot(year_numbers, busses, color='red', label='Bus')
plt.plot(year_numbers, trains, color='blue', label='Rail')
plt.xticks(year_numbers, year_names, fontsize='10')
plt.title("CTA Ridership 2008-2018", fontsize='20')
plt.xlabel("Years", fontsize='15')
plt.ylabel("Riders (hundred millions)", fontsize='15')
plt.legend()

plt.show()

# Explaining trends: The general decline in CTA usage starts at right around
# the time when Uber and other rideshare services became popular. People are
# choosing to take a Lyft instead of the L.
