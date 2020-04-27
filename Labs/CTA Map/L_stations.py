# Folium train map


# 15pts - Use folium to plot all of the L train stops in Chicago. Use an appropriate start zoom level.
# 5pts - Add the name to each stop as a popup. Add a train icon to each marker.  Save as an html page in the same folder.
# 3pts  - Color code all of the lines (make the pink line marker pink etc.)
# 2pts - Brown is not a default color name.  See if you can use the documentation for Folium to set a marker color through other means.

# Data set is in this folder, but can be found at: https://data.cityofchicago.org/api/views/8pix-ypme/rows.csv?accessType=DOWNLOAD

# Tricky parts of this one
## The location is in tuple format.  If you have trouble converting it, try this:
my_string = '(41.2, -87.9)'
my_tuple = eval(my_string)
print(my_tuple)
print(type(my_tuple))


# If you have extra time, try to put some html into the popup.

import folium
import csv
from folium import plugins

with open('CTA_-_System_Information_-_List_of__L__Stops (1).csv') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data.pop(0))
print(data[0])

latlong = [eval(x[-1]) for x in data]
names = [x[2] for x in data]
colors = []

for station in data:
    if station[7] == 'true':
        colors.append('#F23C3C') # red
    elif station[8] == 'true':
        colors.append('#18A1DA') # blue
    elif station[9] == 'true':
        colors.append('#50CB3C') # green
    elif station[10] == 'true':
        colors.append('#825C36') # brown
    elif station[11] == 'true' or station[12 == 'true']:
        colors.append('#7630CB') # purple
    elif station[13] == 'true':
        colors.append('#F5DF37') # yellow
    elif station[14] == 'true':
        colors.append('#F578D9') # pink


cta_map = folium.Map(location=[41.880443, -87.644107],
                     zoom_start=11, tiles="CartoDB positron")

for i in range(len(data)):
    folium.Marker(location=(latlong[i]),
                  popup=names[i],
                  icon=folium.plugins.BeautifyIcon(border_color=colors[i],
                                                   icon='train',
                                                   prefix='fa')
                  ).add_to(cta_map)

cta_map.save('cta_map.html')