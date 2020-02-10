# More on LOOPS

# Basic FOR loop
import random
for i in range(5, 51, 5):
    print(i, end="")

# RANGE function (alternative for comprehension)

# BREAK (breaks out of the loop)

# CONTINUE (skips the rest of this iteration, to the end of the loop

# FOR ELSE
my_list = [x for x in range(1, 101)]
for number in my_list:
    if number == 80:
        print("You UNnaturally finished the loop")
        break
    print(number)
else:
    print("You naturally finished the loop")

# Add me as a collaborator on Github

