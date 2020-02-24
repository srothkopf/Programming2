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

print("--- Linear Search ---") # STEP 4

file = open("../Alice Spellcheck/AliceInWonderLand200.txt") # STEP 5
line_number = 0

def linear_search(key, my_list):
    i = 0
    while i < (len(my_list) - 1) and key.upper() != my_list[i]:  # STEP 10
        i += 1
    if i == len(my_list):
        print(key, "not found")


for line in file: # STEP 7
    line = line.strip().upper()
    line_number += 1
    words = split_line(line) # STEP 8
    for word in words:  # STEP 9
        linear_search(word, words)

file.close() # STEP 12





# Challenge:  Find all words that occur in Alice through the looking glass that do NOT occur in Wonderland.

