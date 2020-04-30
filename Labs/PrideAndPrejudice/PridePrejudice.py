'''
Pride and Prejudice (25pts)

This lab is largely review of: lists, comprehensions, requests, string methods, matplotlib.
The only new item here is using a dictionary (dict).

We will use list, dictionary, and graphing skills to do a basic analysis of Jane Austen's Pride and Prejudice.  Your task
 is to create a bar graph of the 25 most common words.


A common Python pattern to count objects, produce histograms, or update stats is to make calls to a dictionary as you iterate
through a list. For example, given a list of words, you can create a dictionary to store counts and then iterate through the
list of words, checking how many times each word has appeared using your dictionary, and updating the dictionary count now that
you've seen that word again.
'''


# PSEUDO CODE
# Get text from http://www.gutenberg.org/files/1342/1342-0.txt - Use requests library.
# Split the transcript into words - Use split and strip methods and store results in a list.
# Create a dictionary object to store the word counts
# Iterate through the list/text of Pride and Prejudice
# Update word counts on your dict (10pts) {'word1': 5, 'word2': 2 ...}
# Sort words by counts in descending order (5pts) stackoverflow probably?
# Create Bar Graph (5pts)
# Include descriptive titles and labels (5pts)

import requests
import matplotlib.pyplot as plt
import operator

url = "http://www.gutenberg.org/files/1342/1342-0.txt"
pride_prejudice = requests.get(url).text
wordlist = pride_prejudice.split()
wordlist = [x.lower().strip(' ?.,:;!\\<>{}\n\t') for x in wordlist]

url2 = "https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt"
common_words = requests.get(url2).text
common_wordlist = [x.lower().strip(' ?.,:;!\\<>{}\n\t') for x in wordlist]

uncommon_words = []
for word in wordlist:
    if word not in common_words:
        uncommon_words.append(word)
print(uncommon_words)

word_counts = {}
for word in uncommon_words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

org_word_counts = dict(sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)) # thank god for stack overflow

counts = []
for count in org_word_counts:
    counts.append(org_word_counts[count])
org_words = []
for word in org_word_counts:
    org_words.append(word)

top_25_words = org_words[:25]
top_25_counts = counts[:25]

plt.figure(1, tight_layout=True)
plt.barh(top_25_words, top_25_counts, color='red')
plt.yticks(top_25_words, top_25_words)
plt.title("Top 25 Most Used Words in Pride and Prejudice", fontsize=15)
plt.xlabel("Total Uses", fontsize=15)

plt.show()



# CHALLENGE (OPTIONAL)
# Here is a list of the 1000 most common words in English: https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt
# Make your plot show the 25 most common words in Pride and Prejudice NOT in this list.

# MORE CHALLENGES
# look at Project Gutenberg, and try another book and see if your algorithms hold up.
# HERE IS A LIST OF NEGATIVE WORDS.  Evaluate a text for percentage of negative words.   Try the same for positive.  Or do both to evaluate the mood of a book.  Compare Mark Twain to Edgar Allan Poe. https://gist.githubusercontent.com/mkulakowski2/4289441/raw/dad8b64b307cd6df8068a379079becbb3f91101a/negative-words.txt