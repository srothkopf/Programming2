'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!


'''
import turtle

# set up my turtle
my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape('turtle')
my_turtle.speed(0)

# set up my screen
my_screen = turtle.Screen()

# H-Tree
my_screen.bgcolor('turquoise')
my_turtle.color('teal')
my_turtle.width(5)
def recursive_h(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(height / 2)
        my_turtle.left(90)
        my_turtle.forward(height / 2)
        my_turtle.back(height)
        my_turtle.forward(height / 2)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(height / 2)
        my_turtle.back(height)
        recursive_h(x + height / 2, y + height / 2, height / 2,  depth - 1)
        recursive_h(x + height / 2, y - height / 2, height / 2,  depth - 1)
        recursive_h(x - height / 2, y + height / 2, height / 2,  depth - 1)
        recursive_h(x - height / 2, y - height / 2, height / 2,  depth - 1)

recursive_h(0, 0, 315, 4)
my_screen.clear()

my_screen.bgcolor('black')
my_turtle.color('white')
my_turtle.width(0)

# Sierpenski Triangles
def sier_triangles(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(height / 2)
        my_turtle.right(120)
        my_turtle.forward(height)
        my_turtle.right(120)
        my_turtle.forward(height)
        my_turtle.right(120)
        my_turtle.forward(height/2)
        sier_triangles(x, y + height / 2, height / 2, depth - 1)
        sier_triangles(x + height / 2, y - height / 2, height / 2, depth - 1)
        sier_triangles(x - height / 2, y - height / 2, height / 2, depth - 1)

sier_triangles(0, 25, 250, 5)

my_screen.bgcolor('beige')
my_turtle.color('blue')
my_turtle.width(2)

def my_fractal(x, y, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.setheading(90)
        my_turtle.forward(height)
        for i in range(4):
            my_turtle.left(20)
            my_turtle.forward(height / 2)
        for i in range(4):
            my_turtle.back(height / 2)
            my_turtle.right(20)
        for i in range(4):
            my_turtle.right(20)
            my_turtle.forward(height / 2)
        for i in range(4):
            my_turtle.back(height / 2)
            my_turtle.left(20)
        my_fractal(x + height * 1.43, y + height * 2.2, height / 2, depth - 1)
        my_fractal(x - height * 1.43, y + height * 2.2, height / 2, depth - 1)


my_fractal(0, -300, 120, 6)

my_screen.exitonclick()



