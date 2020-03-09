# exceptions (use sparingly)

x = 2
y = 0

# divide by zero (zero division error)
try:
    print(x / y)
except:
    print("Infinity")


# conversion error (value error)
try:
    int("T")
except:
    print("Number was not valid")

# handle with a loop
done = False
while not done:
    try:
        user_input = int(input("Enter an integer: "))
        done = True
    except:
        print("Number is not valid")

# file opening (ioerror, file not found error)
try:
    file = open("AliceInWonderland.txt")
except:
    print("Could not open file")

# use built in error types for python to check what error occured.
try:
   # my_file = open("my_file.txt")
    #int("Hello")
    print(1/0)
except FileNotFoundError:
    print("File not found")
except ValueError as e:
    print("Invalid conversion")
    print(e)
except ZeroDivisionError as e:
    print("Error", e)