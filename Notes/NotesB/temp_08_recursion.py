# Recursion - function calling itself

def f():
    print("f")

def g():
    print("g")
    f()
    # g() # Recursion error
    print("END") # never prints

g() # error commented out

# control recursion with depth

def controlled(depth):
    print("recursion depth", depth)
    if depth > 0:
        controlled(depth - 1)
    print("recursion depth", depth," has closed.")

controlled(10)

