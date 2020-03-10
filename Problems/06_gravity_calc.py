# Universal Gravity Calculator (12pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (2pts) keeps asking for inputs until they are valid (see while loop from notes)
# (3pts) calculates the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.


print("WELCOME TO UNIVERSAL GRAVITY CALCULATOR")
print("Please enter the following information:")
gravity = 6.67e-11

def grav_calc(m1, m2, r):
    done = False
    while not done:  # (3pts) takes the inputs for mass 1, mass 2, and distance between the two objects (m1, m2, and r)
        try:
            answer = gravity * (m1 * m2) / r ** 2
            print("The force of gravity between the two objects is {:.2e} Newtons.".format(answer))
            done = True
        except ZeroDivisionError:
            print("Error, the distance cannot equal 0.")
            done = True

done = False
while not done:
    try:
        mass_1 = int(input("Mass of object 1(kg):"))
        mass_2 = int(input("Mass of object 2(kg):"))
        r = int(input("Distance between the objects(center to center, meters):"))
        grav_calc(mass_1, mass_2, r)
        done = True
    except ValueError:
        print("Invalid input")



