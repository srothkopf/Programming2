# Formatting numbers
import random

#round function: round(n, digits)
print(round(3.141592653589753238462643383279502881796, 2))

# format method (string method)
a = 9384355
b = 345.8934567890987654
print("My number is {}".format(a)) # {} is the formatted number "a"
print("My number is {:.3f}".format(b))
print("My numbers are {} and {}".format(a, b)) # places them sequentially unless otherwise
print("My numbers are {1:.3f} and {0:,}".format(a, b)) # specifics

# order: spaceholder+justification+width+commas+precision+datatype+notation


# fixed width/spacing
for i in range(20):
    c = random.randrange(100000)
    print("${:4}".format(c))

 # justification (^center, <left, >right)
for i in range(20):
    c = random.randrange(-10000, 10000)
    print("{:^12} dollars".format(c))

# add commas
for i in range(20):
    c = random.randrange(-10000, 10000)
    print("{:12,}".format(c))

# precision (f float, d dec/int, b binary)
for i in range(20):
    c = random.random()
    print("{:<11.5f}".format(c))

for i in range(20):
    c = random.randrange(10000)
    print("{:b} ".format(c)) # b for binary

# scientific notation
for i in range(20):
    c = random.random()
    print("{:.2e}".format(c)) # scinot to two decimal