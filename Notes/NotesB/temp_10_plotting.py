# Plotting (with matplotlib)
import matplotlib.pyplot as plt

plt.figure(1) # creates a new plot/window

plt.plot([1, 2, 3, 3]) # plots a y against the index x
plt.plot([1, 2, 3, 4], [12, 8, 2, 1]) # plots x then y ([x points], [y points])

plt.figure(2) # new window/plot

x_points = [x for x in range(1, 11)]
y_points = [y ** 2 for y in x_points]

plt.plot(x_points, y_points, color='red', marker='*', markersize= '10', linestyle='--', alpha=1, mec='black')

#TALUNK (title, axes, labels, units, numbers, key)

plt.title("Example Plot") #Title
plt.xlabel("Time(s)", color='red', fontsize='20')
plt.ylabel("Excitement (Yays!)", color='red', fontsize='20')
plt.axis([0, 11, 0, 110]) # [xmin, xmax, ymin, ymax]


plt.show()

