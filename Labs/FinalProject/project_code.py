import csv
import matplotlib.pyplot as plt
import numpy as np

with open("datasets_569763_1033439_WHR20_DataForFigure2.1.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

header = data.pop(0) # remove headers, get data columns
print(header)

# list set up
countries = []
happy_score = []
corruption_score = []
support_score = []
freedom_score = []

for country in data:
    try: # check for invalid data
        happy = float(country[2])
        corruption = float(country[11])
        support = float(country[7])
        freedom = float(country[9])
        name = country[0]

        happy_score.append(happy * 10)
        corruption_score.append(corruption * 100)
        support_score.append(support * 100)
        freedom_score.append(freedom * 100)
        countries.append(name)
    except:
        print(country[0], "data is invalid")

plt.figure("Happiness vs. Corruption", figsize=(10, 6)) # fig 1

# create plot
plt.scatter(corruption_score, happy_score, color='orange')
plt.ylabel("Happiness Score (out of 100)")
plt.xlabel("Perceptipon of Corruption Score (out of 100)")
plt.title("Happiness vs. Perception of Corruption By Country 2020")

# label data points with respective country names
for i in range(len(countries)):
    plt.annotate(countries[i], xy=(corruption_score[i], happy_score[i]), fontsize=5)

# best fit line
p = np.polyfit(corruption_score, happy_score, 2)
x = [x for x in range(100)]
y = [p[0] * y + p[1] for y in x]
y = [p[0] * y ** 2 + p[1] * y + p[2] for y in x]
plt.plot(x, y, color='red')

plt.show()

plt.figure("Happiness vs. Social Support", figsize=(10, 6)) # fig 2

# create plot
plt.scatter(support_score, happy_score, color='orange')
plt.ylabel("Happiness Score (out of 100)")
plt.xlabel("Social Support Score (out of 100)")
plt.title("Happiness vs. Social Support By Country 2020")

# label data points with respective country names
for i in range(len(countries)):
    plt.annotate(countries[i], xy=(support_score[i], happy_score[i]), fontsize=5)

# best fit line
p = np.polyfit(support_score, happy_score, 2)
x = [x for x in range(100)]
y = [p[0] * y + p[1] for y in x]
y = [p[0] * y ** 2 + p[1] * y + p[2] for y in x]
plt.plot(x, y, color='red')

plt.show()

plt.figure("Corruption vs. Freedom", figsize=(10, 6)) # fig 3

# create plot
plt.scatter(freedom_score, corruption_score, color='orange')
plt.ylabel("Corruption Score (out of 100)")
plt.xlabel("Freedom Score (out of 100)")
plt.title("Perception of Corruption vs. Freedom By Country 2020")

# label data points with respective country names
for i in range(len(countries)):
    plt.annotate(countries[i], xy=(freedom_score[i], corruption_score[i]), fontsize=5)

# best fit line
p = np.polyfit(freedom_score, corruption_score, 2)
x = [x for x in range(100)]
y = [p[0] * y + p[1] for y in x]
y = [p[0] * y ** 2 + p[1] * y + p[2] for y in x]
plt.plot(x, y, color='red')

plt.show()

