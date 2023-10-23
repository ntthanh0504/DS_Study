import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

# Turtorial
""" wn.title("Turtorial")

def draw_bar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height) # Draw up the left side
    t.write(' ' + str(height)) 
    t.right(90)
    t.forward(40) # Width of bar, along the top
    t.right(90)
    t.forward(height) # And down again!
    t.left(90) # Put the turtle facing the way we found it.
    t.end_fill() 
    t.forward(10) # Leave small gap after each bar

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]

for v in xs: # Assume xs and tess are ready
    draw_bar(tess, v) """

# Ex 7, 8, 9
wn.title("Ex 7")

def draw_bar(t, height):
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(height) # Draw up the left side
    t.write(' ' + str(height)) 
    t.right(90)
    t.forward(40) # Width of bar, along the top
    t.right(90)
    t.forward(height) # And down again!
    t.left(90) # Put the turtle facing the way we found it.
    t.end_fill()
    t.penup() 
    t.forward(10) # Leave small gap after each bar

tess = turtle.Turtle()
tess.pensize(3)

xs = [-83, 75, 74.9, 100, 69.9, 210, 60, 59.9, 55, 50,49.9, 45, 44.9, 40, 39.9, 2, 0]

for v in xs: # Assume xs and tess are ready
    if v >= 200:
        tess.color("blue", "red")
    elif v >= 100:
        tess.color("blue", "yellow")
    else:
        tess.color("blue", "green")
    draw_bar(tess, v)

wn.mainloop()

# 