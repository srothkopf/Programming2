'''
Searching problems (25pts)
Complete the following 3 searching problems using techniques
from class and from the notes and the textbook website.
Solutions should use code to find and print the answer.
'''
import re

def split_line(line):
    # uses regular expressions to split line of text into word list
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.


file = open("../Searching/dictionary.txt")
word_list = []

for line in file:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        word_list.append(word)

length_numbers = []
length_list = []
for word in word_list:
    length = len(word)
    length_numbers.append(length)
    length_numbers.sort()
    if length == length_numbers[-1]:
        length_list.append(word)
print("The longest word in our abridged dictionary is", length_list[-1])


# 2.  (8pts)  Write code which finds the total word count AND average word length
# in "AliceInWonderLand.txt"

alice = open("../Searching/AliceInWonderLand.txt")
alice_word_list = []

for line in alice:
    line = line.strip().upper()
    words = split_line(line)
    for word in words:
        alice_word_list.append(word)
print("There are a total of",len(alice_word_list),"words in Alice in Wonderland.")

word_lengths = [len(word) for word in alice_word_list]
print("The average word length in Alice in Wonderland is",(sum(word_lengths))/len(alice_word_list))

# 3.  (3pts)  How many times does the name Alice appear in Alice in Wonderland?

def count_occurances(key):
    word_list = []
    for word in alice_word_list:
        if word == key:
            word_list.append(word)
    return len(word_list)

print("The word 'Alice' occurs",count_occurances("ALICE"),"times in Alice in Wonderland.")

# 4.  (6pts) Find the most frequently occurring seven letter word in "AliceInWonderLand.txt"
seven_letter_words = []
for word in alice_word_list:
    if len(word) == 7:
        seven_letter_words.append(word)

repeats = []
freq_list = []
for word in seven_letter_words:
    frequency = seven_letter_words.count(word)
    repeats.append(frequency)
    repeats.sort()
    if frequency == repeats[-1]:
        freq_list.append(word)
print("The most common seven letter word in Alice in Wonderland "
      "is '",(freq_list[-1]).lower(),"'. (It occurs",repeats[-1],"times)")

# 5.  (2pts, small points challenge problem)
# How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
print("The word 'Cheshire' occurs",count_occurances("CHESHIRE"),"times in Alice in Wonderland.")

# How many times does "Cat" occur?
print("The word 'Cat' occurs",count_occurances("CAT"),"times in Alice in Wonderland.")

# How many times does "Cheshire" immediately followed by "Cat" occur?




