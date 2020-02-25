'''
Complete the chapter lab at https://docs.google.com/document/d/1KjrNiE3mUbaeyTPpaTesAlnVYkp0KkkM-17oOKqscjw/edit?usp=sharing
'''

# Successful linear spellcheck (10pts)
# Successful binary spellcheck (10pts)
# Binary and linear are written as functions (5pts)

import re

def split_line(line):
    # This function takes in a line of text and returns
    # a list of words in the line.
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line) # STEP 1

file = open("../Alice Spellcheck/dictionary.txt") # STEP 2
with open("../Alice Spellcheck/dictionary.txt") as f:
    dictionary_words = [x.strip().upper() for x in f]
file.close() # STEP 3

'''
print("--- Linear Search ---") # STEP 4

file = open("../Alice Spellcheck/AliceInWonderLand200.txt") # STEP 5
line_number1 = 0

def linear_search(key, my_list, line_number):
    i = 0
    while i < (len(my_list) - 1) and key.upper() != my_list[i]:  # STEP 10
        i += 1
    if i >= len(my_list) - 1:
        print(key, "on line number", line_number, "was not found in the dictionary.") # STEP 14

for line in file: # STEP 7
    line = line.strip().upper()
    line_number1 += 1
    words = split_line(line) # STEP 8
    for word in words:  # STEP 9
        linear_search(word, dictionary_words, line_number1)

file.close() # STEP 11
''' # STEP 16

print("--- Binary Search ---") # STEP 15

file = open("../Alice Spellcheck/AliceInWonderLand200.txt")
line_number2 = 0

def binary_search(key, my_list, line_number): # STEP 17
    lower_bound = 0
    upper_bound = len(my_list) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if my_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif my_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    if not found:
        print(key, "on line number", line_number, "was not found in the dictionary.")

for line in file:
    line = line.strip().upper()
    line_number2 += 1
    words = split_line(line)
    for word in words:
        binary_search(word, dictionary_words, line_number2)

file.close()
pat_self_on_back = True # STEP 21

# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.

print("\n--- Challenge Problem ---")
file = open("../Alice Spellcheck/AliceInWonderLand.txt")
file2 = open("../Alice Spellcheck/AliceThroughTheLookingGlass.txt")
looking_glass_words = []
wonderland_words = []
line_number3 = 0

for line in file2:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        looking_glass_words.append(word)
        looking_glass_words.sort()
for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        wonderland_words.append(word)
        wonderland_words.sort()

def challenge_binary_search(key, my_list, line_number): # STEP 17
    lower_bound = 0
    upper_bound = len(my_list) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (upper_bound + lower_bound) // 2
        if my_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif my_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    if not found:
        print(key, "on line number", line_number, "was not found in Alice in Wonderland.")

for word in looking_glass_words:
    line_number3 += 1
    challenge_binary_search(word, wonderland_words, line_number3)

file.close()