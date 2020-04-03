
'''
Greenhouse gas emissions (GHG) vs. square footage for all school buildings in Chicago

Data set used will be Chicago Energy Benchmark info from 2018
data can be found at...
https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD

Energy Efficiency of Chicago Schools (35pts)

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2015 to 2018.
We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
Challenge (for fun):
An efficient school would have a large ratio of sqft to ghg.
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:
- Scatter plot the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (10pts)
- Data includes ONLY data for K-12 Schools. (5pts)
- Data includes ONLY data for 2018 reporting. (5pts)
- Label x and y axis and give appropriate title. (5pts)
- Annotate Francis W. Parker. (5pts)
- Create a best fit line for schools shown. (5pts)


Extra Credit: Add a significant feature to your graph that helps tell the story of your data.  (feel free to use methods from matplotlib.org). (10pts)

Note: With extra credit you will earn you a max of 35pts (100%) for the assignment.
Maybe you can try one of the following or think up your own:
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)


Note 2:  This is a tough assignment to do on your own.  Do your best with what you have.
'''

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("Chicago_Energy_Benchmarking (1).csv") as f:
    reader = csv.reader(f)
    data = list(reader)

header = data.pop(0)
print(header)

ghg_index = header.index("Total GHG Emissions (Metric Tons CO2e)")
sqft_index = header.index("Gross Floor Area - Buildings (sq ft)")
type_index = header.index("Primary Property Type")

valid_data = []

for building in data:
    try:
        int(building[ghg_index])
        int(building[sqft_index])
        if building[type_index] == "K-12 School" and building[0] == "2018":
            valid_data.append(building)
    except:
        pass


ghg = [int(x[ghg_index]) for x in valid_data]

color = []
for building in ghg:
    if building > 4000:
        color.append("red")
    else:
        color.append("green")

sqft = [int(x[sqft_index]) for x in valid_data]

names = [x[2] for x in valid_data]
print()
print(names)


plt.figure(1, tight_layout=True)
plt.scatter(sqft, ghg, c=color) # s for size, c for color
plt.title("Chicago K-12 Schools 2018 GHG Emissions", fontsize='20')
plt.xlabel("Building Size (sq ft)", fontsize='15')
plt.ylabel("GH Gas Emissions (tons CO2)", fontsize='15')

plt.annotate("Latin School of Chicago Upper School", xy=(151751, 1780)) # Parker's 2018 data must not be valid
# it doesn't show up in my data so I just decided to use Latin instead

p = np.polyfit(sqft, ghg, 1) # best fit
x = [x for x in range(500000)]
y = [p[0] * y + p[1] for y in x]
plt.plot(x, y)

plt.show()