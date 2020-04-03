import csv
import requests
import matplotlib.pyplot as plt
import numpy as np


def get_data(url):
    with requests.Session() as s:
        download = s.get(url)
        content = download.content.decode('utf-8')
        reader = csv.reader(content.splitlines(), delimiter=',')
        my_list = list(reader)
    return my_list

data = get_data(url = "https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD")

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

p = np.polyfit(sqft, ghg, 1) # best fit
print(p)
x = [x for x in range(500000)]
y = [p[0] * y + p[1] for y in x]
plt.plot(x, y)

plt.show()
