# Searching and read/write files

# forward slash goes into a directory. ".." goes "up" a directory
# by default, open() opens a file to read ('r') (does 'r' automatically)
file = open('../resources/super_villains.txt', 'r')
print(file)
file.close() # ends your access to the file

# Open a file to write with  'w'
# Overwrites entire file

# Open a file to append with 'a'
file = open('../resources/super_villains.txt', 'a')
file.write("\nMia the Horrible")
file.close()

# Go through the info in the file line by line
file = open('../resources/super_villains.txt', 'r')
for line in file:
    print(line.strip().upper())

file.close()

# .strip() method strips out spaces, tabs, returns (/t, /n etc.)
print(("Hi\n").strip())
print(("     Hello").strip())

# Better way to open files (syntactic sugar)
with open('../resources/super_villains.txt') as f:
    for line in f:
        print("Hello", line.strip().upper())

# REad data into a list (array)
with open('../resources/super_villains.txt') as f:
    villains = [x.strip().upper() for x in f]

print(villains)

# Linear search
# Python way
print("VARVARA TEMPEST" in villains)  # in keyword

# brute force way
i = 0
key = "VARVARA TEMPEST"
while i < (len(villains) - 1) and key != villains[i]:
    i += 1

if i < (len(villains) - 1):
    print("Found", key, "at position", i)
else:
    print(key, "not found.")

# make a function out of it!
def linear_search(key, my_list):
    """
    Searches for key inside of list and returns True if you find it.
    :param key: item to find
    :param my_list: list to find key in
    :return: bool found
    """
    i = 0
    while i < (len(my_list) - 1) and key.upper() != my_list[i]:
        i += 1

    if i < (len(my_list) - 1):
        print("Found", key, "at position", i)
        return True
    else:
        print(key, "not found.")
        return False

print(linear_search("SCARLETINA OF GRIMOIRE", villains))

# Binary Search
villains.sort()

key = "RUPERT THE ENCHANTER"
lower_bound = 0
upper_bound = len(villains) - 1
found = False

while lower_bound <= upper_bound and not found:
    middle_pos = (upper_bound + lower_bound) // 2
    if villains[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villains[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True

if found:
    print(key, "found at position", middle_pos)
else:
    print(key, "was not found")

# GIFTED FUNCTION
# returns a list of words in each line

import re # regular expression

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

my_text = "Romeo, Romeo, wherefore art thou Romeo."
print(split_line(my_text))
file = open("../resources/alice_in_wonderland")

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        print(word)
