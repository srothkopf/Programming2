# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(101)]
# b) Make a list of even numbers from 20 to 40
my_evenlist = [x for x in range(20,41)if x ** 2 % 2 == 0]
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_squarebois = [x ** 2 for x in range(101)]
# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
my_poslist = [x for x in my_list if x >= 0]

# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list
from Problems import number_list
print(number_list.num_list[-5:])

# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(number_list.num_list))
# Find and print the lowest number in num_list (1pt)
print(min(number_list.num_list))
# Find and print the average of num_list (2pts)
print(sum(number_list.num_list)/len(number_list.num_list))
# Remove the lowest number from num_list (2pt)
number_list.num_list.sort()
number_list.num_list.pop(0)
# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)
top_ten = number_list.num_list[-10:]
print(top_ten)

# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?
repeats = []
freq_list = []
for number in number_list.num_list:
    frequency = number_list.num_list.count(number)
    repeats.append(frequency)
    repeats.sort()
    if frequency == repeats[-1]:
        freq_list.append(number)
print(freq_list[-1])
# yay 3507
# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't

# Find the number of palindromes
# Hint: This may be easier to do with strings
palindromes = []
for number in number_list.num_list:
    str_num_list = [int(char) for char in str(number)]
    if str_num_list[0] == str_num_list[3] and str_num_list[1] == str_num_list[2]:
        palindromes.append(number)
print(len(palindromes))


