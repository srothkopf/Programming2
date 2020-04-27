# Dictionaries (dict)

# list, tuple, int, float, bool, str, set, dict

# Sets ( not generally used often )
# unique list of items (no repeats)
# uses {} instead of []

my_set = {1, 2, 3, 4, 4, 5}
print(my_set) # gets rid of extra 4

my_list = ['milk', 'toilet paper', 'yeast', 'strawberries', 'milk']
print(set(my_list)) # gets rid of extra milk, curly bracks

# gets rid of duplicates
my_list = list(set(my_list))
print(my_list) # square bracks
print(type(my_list))

# Dictionaries
# why use dictionaries?
# {key1: val1, key2: val2...}
star = ['Star', 16, 'English', 'Python']
star = {'first name': 'Star', 'age': 16, 'spoken language': ['English', 'Spanish'], 'fav prog lang': 'Python'}
print(star)

# TV shows
the_office = {'genre': ['Mockumentary','Sitcom'],
              'developedBy': 'Greg Daniels',
              'starring': ['Steve Carell', 'Rainn Wilson', 'John Krasinski', 'Jenna Fischer']}

# acc3ss a dict
print(the_office['genre'])
# print(the_office[0]) # produces key error

# add to a dictionary
the_office['no. seasons'] = 9
print(the_office)
the_office['title'] = "The Office"


# change value
the_office['no. seasons'] += 1
print(the_office)

# add to values
the_office['starring'].append('Mindy Kaling')
print(the_office)

# what are my keys?
print()
print(the_office.keys()) # iterable dict_key object
print(the_office.values()) # dict_values object

parks_rec = {"title": "Parks and Recreation",
             "created by": ["Greg Daniels", "Michael Schur"]}

shows = [the_office, parks_rec]
print()
print(shows)
print()


for key in the_office:
    print(the_office[key])

# even comprehensions work
new_dict = {x: "Hi" for x in range(10)}
print(new_dict)

# popping items
print(the_office.pop('developedBy'))
print(the_office)
