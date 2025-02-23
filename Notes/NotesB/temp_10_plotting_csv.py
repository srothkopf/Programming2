import matplotlib.pyplot as plt
import csv

with open("Libraries_-_2019_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
print(headers)

data.sort(key=lambda x: int(x[-1]))

library_names = [x[0] for x in data]
print(library_names)

monthly_data = [x[4:-1] for x in data]
print(monthly_data)

my_library = monthly_data[library_names.index('Lincoln Park')]
my_library = [int(x) for x in my_library]
print(my_library)

library2 = monthly_data[library_names.index('Bucktown-Wicker Park')]
library2 = [int(x) for x in library2]

plt.figure(1, tight_layout=True)
month_numbers = [x for x in range(12)]
month_names = headers[4:-1]

plt.plot(month_numbers, library2, color='blue', label='Bucktown')
#plt.plot(month_numbers, my_library) # plots line graph
plt.plot(month_numbers, my_library, color='teal', label='Lincoln Park') # plots bar graph
plt.xticks(month_numbers, month_names, fontsize='5') # replaces the shown values on the graph axis
plt.axis([-1,12,0,16000])
plt.title("Library Visitors 2019", fontsize='20')
plt.xlabel("Months", fontsize='10')
plt.ylabel("Visitors", fontsize='10')
plt.legend()

plt.figure(2, tight_layout=True, figsize=(8,8))

# plot every library in Chicago YTD visitors
# get library totals
ytd_totals = [int(x[-1]) for x in data]
print(ytd_totals)

library_numbers = [x for x in range(len(library_names))]

plt.barh(library_numbers, ytd_totals)
plt.yticks(library_numbers, library_names, fontsize='6')
plt.title("Annual Visitors to Chicago Public Libraries 2019")
plt.xlabel("Total Visitors", fontsize='10')

plt.show()