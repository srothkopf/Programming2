'''
Turtle is an introductiory graphics program for learning

'''
import turtle

# set up my turtle
my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_turtle.shape('turtle')
my_turtle.speed(0)

# set up my screen
my_screen = turtle.Screen()
my_screen.bgcolor('white')

# draw a shape using goto method (red square)
my_turtle.fillcolor('teal')
my_turtle.begin_fill() # starts a shape which will be filled
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill()

# draw shape using headings
my_turtle.up()
my_turtle.goto(-200, 200)
my_turtle.down()
my_turtle.setheading(270) # face south
my_turtle.fillcolor("lavender")
my_turtle.begin_fill()

for i in range(8):
    my_turtle.forward(50)
    my_turtle.left(45)

my_turtle.end_fill()

my_screen.clear()

def recursive_rect(width, height, depth):
    if depth > 0:
        my_turtle.width(depth)
        my_turtle.up()
        my_turtle.goto(width/2, height/2) # top right
        my_turtle.down()
        my_turtle.goto(-width/2, height/2) # top left
        my_turtle.goto(-width/2, -height/2) # bottom left
        my_turtle.goto(width/2, -height/2) # bottom right
        my_turtle.goto(width / 2, height / 2)  # top right
        recursive_rect(width/1.5,height/1.5,depth -1)

recursive_rect(900,600,10)

my_screen.clear()

def recursive_ncaa(x,y,height,depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x,y)
        my_turtle.down()
        my_turtle.setheading(0)
        my_turtle.forward(50)
        my_turtle.left(90)
        my_turtle.forward(height / 2)
        my_turtle.right(90)
        my_turtle.forward(50)
        my_turtle.right(180)
        my_turtle.forward(50)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(90)
        my_turtle.forward(50)
        recursive_ncaa(x + 100, y + height / 2, height / 2, depth - 1)
        recursive_ncaa(x + 100, y - height / 2, height / 2, depth - 1)

recursive_ncaa(-350, 0, 300, 7)








my_screen.exitonclick()