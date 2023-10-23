# list of permitted color: https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html

import turtle

# Turtorial 1
""" wn = turtle.wn() # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle() # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle() # Create alex

for i in range(3):
    tess.forward(80) # Make tess draw equilateral triangle
    tess.left(120)
    
tess.right(180) # Turn tess around
tess.forward(80) # Move her away from the origin

colors = ["yellow", "red", "purple", "blue"]

for i, color in enumerate(colors):
    alex.color(color)
    alex.forward(50)
    alex.left(90)

alex.penup()
alex.forward(100) # This moves alex, but no line is drawn
alex.pendown()
alex.shape("turtle")

wn.mainloop() """

# Turtorial 2
""" wn = turtle.wn()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup() # This is new
size = 20
for i in range(30):
    tess.stamp() # Leave an impression on the canvas
    size = size + 3 # Increase the size on every iteration
    tess.forward(size) # Move tess along
    tess.right(24) # ... and turn her

wn.mainloop() """

# Ex 6
""" wn = turtle.wn()
wn.bgcolor("lightgreen")
wn.title("Ex 6")

this_dict = {'equilateral_triangle': ['red', 3, 120], 'square': ['blue', 4, 90], 'hexagon': ['yellow', 6, 60], 'octagon': ['purple', 8, 45]}

for value in this_dict.values():
    polygon = turtle.Turtle()
    polygon.color(value[0])
    
    for i in range(value[1]):
        polygon.forward(50)
        polygon.left(value[2])
    
wn.mainloop() """

# Ex 10
""" wn = turtle.wn()
wn.bgcolor("lightgreen")
wn.title("Ex 10")

tess = turtle.Turtle()
tess.right(90)
tess.left(3600)
tess.right(-90)
tess.speed(10)
tess.left(3600)
tess.speed(0)
tess.left(3645)
tess.forward(-100)

wn.mainloop() """

# Ex 11
""" wn = turtle.wn()
wn.bgcolor("lightgreen")
wn.title("Ex 11")

tess = turtle.Turtle()
tess.shape('turtle')
tess.penup()

tess.forward(100)
for _ in range(5):
    tess.forward(150)
    tess.right(144)
    
wn.mainloop() """

# Ex 12

wn = turtle.Screen()
wn.setup(500, 500)
clk = turtle.Turtle()
clk.color('Green')
clk.width(4)

def draw_hour_hand():
	clk.penup()
	clk.home()
	clk.right(90)
	clk.pendown()
	clk.forward(100)

val = 0

for i in range(12):
	val += 1
	clk.penup()
	clk.setheading(-30 * (i + 3) + 75)
	clk.forward(22)
	clk.pendown()
	clk.forward(15)
	clk.penup()
	clk.forward(20)

	clk.write(str(val), align="center", font=("Arial", 12, "normal"))

clk.setpos(2, -112)
clk.pendown()
clk.width(2)

clk.fillcolor('Green')
clk.begin_fill()
clk.circle(5)
clk.end_fill()

clk.penup()
draw_hour_hand()
clk.setpos(-20, -64)
clk.pendown()
clk.penup()

clk.setpos(-30, -170)
clk.pendown()
clk.write(' GfG Clock', font=("Arial", 14, "normal"))
clk.hideturtle()

turtle.done()
