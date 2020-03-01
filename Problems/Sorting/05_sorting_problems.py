'''
Sorting and Intro to Big Data Problems (22pts)

Import the data from NBAStats.py.  The data is all in a single list called 'data'.
I pulled this data from the csv in the same folder and converted it into a list for you already.
For all answers, show your work
Use combinations of sorting, list comprehensions, filtering or other techniques to get the answers.
'''
from NBAStats import data

#1  Pop off the first item in the list and print it.  It contains the column headers. (1pt)
column_headers = data.pop(0)
print(column_headers)

#2  Print the names of the top ten highest scoring single seasons in NBA history?
# You should use the PTS (points) column to sort the data. (4pts)
data.sort(reverse=True, key=lambda a: a[-1])
top_ten = [x for x in data[:10]]
print("The top ten scoring seasons ever were scored in order by:")
rank = 0
for player in top_ten:
    rank += 1
    print(rank,".)",player[2], "(", player[-1], "points)")

#3  How many career points did Kobe Bryant have? Add up all of his seasons. (4pts)
bryant = []
bryant_pts = []
for player in data:
    if player[2] == "Kobe Bryant":
        bryant.append(player)

for stat in bryant:
    bryant_pts.append(stat[-1])

career_pts = sum(bryant_pts)
print("Kobe Bryant scored a total of", career_pts, "career points.")

#4  What player has the most 3point field goals in a single season. (3pts)
data.sort(reverse=True, key=lambda a: a[-19])
print(data[0][2], "scored the most 3-point field goals in a single season (",data[0][-19],").")

#5  One stat featured in this data set is Win Shares(WS).
data.sort(reverse=True, key=lambda a: a[25])
#  WS attempts to divvy up credit for team success to the individuals on the team.
#  WS/48 is also in this data.  It measures win shares per 48 minutes (WS per game).
#  Who has the highest WS/48 season of all time? (4pts)
print(data[0][2], "has the highest WS/48 season of all time(",data[0][25],").")

#6  Write your own question that you have about the data and provide an answer (4pts)
# Maybe something like: "Who is the oldest player of all time?"  or "Who played the most games?"  or "Who has the most combined blocks and steals?".
# Who is the oldest player of all time? (I'm genuinely curious)
data.sort(reverse=True, key=lambda a: a[4])
print(data[0][2], "was the oldest player of all time (", data[0][4],"years old).")

#7  Big challenge, few points.  Of the 100 highest scoring single seasons in NBA history, which player has the
# worst free throw percentage?  Which had the best? (2pts)
data.sort(reverse=True, key=lambda a: a[-1])
top_hundred = [x for x in data[:100]]
top_hundred.sort(reverse=True, key=lambda a: a[-10])
print("Out of the top 100 scoring single seasons in NBA history,", top_hundred[0][2], "had the worst free throw "
        "percentage and", top_hundred[-1][2], "had the best.")
print("(The difference between them was", (top_hundred[0][-10] - top_hundred[-1][-10]) * 100, "%)")







