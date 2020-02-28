# Sorting
import random
import time

# Swap values
a = 1
b = 2

temp = a
a = b
b = temp

print(a, b)

# pythonic way
a, b = b, a # works only in python

print(a, b)

# make a random list of 100 numers with values from 1 to 99
my_list = [random.randrange(1,100) for x in range(100)]
my_list2 = my_list[:]

def count_nices(list):
    nices = []
    for num in my_list:
        if num == 69:
            nices.append(num)
    return (len(nices))

print(my_list)

for cur_pos in range(len(my_list)):
    min_pos = cur_pos
    for scan_pos in range(cur_pos + 1, len(my_list)):
        if my_list[scan_pos] < my_list[min_pos]:
            min_pos = scan_pos
    my_list[cur_pos], my_list[min_pos] = my_list[min_pos], my_list[cur_pos]

print(my_list)

# Insertion Sort
print(my_list2)

for key_pos in range(1, len(my_list2)):
    key_val = my_list2[key_pos]
    scan_pos = key_pos - 1 # look to dancer's left
    while scan_pos >= 0 and key_val < my_list2[scan_pos]:
        my_list2[scan_pos + 1] = my_list2[scan_pos]
        scan_pos -= 1
    my_list2[scan_pos + 1] = key_val
print(my_list2)

print(count_nices(my_list2))

# Optional function parameters

print("Merp", end=" ")
print("World", end="!")
print("\nHello", "Morld", sep="Big",end="!!!\n")

def hello(name, time_of_day="morning"):
    print("Hello", name, "good", time_of_day)

hello("Star", "afternoon")
hello("Mia")
hello("James", time_of_day="evening")


# Lamba functions
# When you need a function, but dont want to make a function
# Also called anonymous functions

# lambda parameter: returned
double_me = lambda x: x * 2
print(double_me(5))

product = lambda a, b: a * b
print(product(4,6))

# Real world sorting with python
my_list = [random.randrange(1,100) for x in range(100)]
print(my_list)

my_2dlist = [[random.randrange(1,100), random.randrange(1,100)]for x in range(100)]
print(my_2dlist)

# sort method (changes the list in place)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

my_2dlist.sort(key=lambda a: a[0])
print(my_2dlist)
my_2dlist.sort(key=lambda a: a[1])
print(my_2dlist)
my_2dlist.sort(reverse=True, key=lambda a: sum(a))
print(my_2dlist)

# sorted function (returns a new list)
new_list = sorted(my_2dlist, reverse=True, key=lambda x: abs(x[0]-x[1]))
print(new_list)

