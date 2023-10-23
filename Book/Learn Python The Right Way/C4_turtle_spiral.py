import turtle

# Turtorial

""" def draw_multicolor_square(t, sz):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

size = 20 # Size of the smallest square
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10 # Increase the size for next time

    tess.forward(10) # Move tess along a little
    tess.right(18) # and give her some turn

wn.mainloop() """

# Ex 1

""" wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Ex 1")


def draw_a_square(t, sz):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)
        
tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

for _ in range(5):
    draw_a_square(tess, 20)
    tess.penup()
    tess.forward(50)
    tess.pendown()
    
wn.mainloop() """

# Ex 2

""" wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Ex 2")


def draw_a_square(t, sz):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)
        
tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)
size = 20
for _ in range(5):
    draw_a_square(tess, size)
    tess.penup()
    tess.right(135)
    tess.forward(15)
    tess.left(135)
    tess.pendown()
    size += 20
    
wn.mainloop() """

# Ex 3

""" wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Ex 3")

def draw_poly(t, n, sz):
    for _ in range(n):
        t.forward(sz)
        t.left(45)

tess = turtle.Turtle()
tess.pensize(3)
tess.color('purple')

n, size = 8, 20
draw_poly(tess, n, size)

wn.mainloop() """

# Ex 4

""" wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Ex 4")

def draw_a_square(t, sz):
    for _ in range(4):
        t.forward(sz)
        t.left(90)
        
    for _ in range(4):
        t.backward(sz)
        t.left(90)
        
    for _ in range(4):
        t.left(90)
        t.forward(sz)
        
    for _ in range(4):
        t.left(90)
        t.backward(sz)
        

tess = turtle.Turtle()
tess.pensize(3)
tess.color('blue')

n, size = 8, 100
for _ in range(6):
    tess.speed(10)
    draw_a_square(tess, size)
    tess.right(15)

wn.mainloop() """

# Ex 5

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Ex 4")

def draw_a_square(t, sz):
    for _ in range(4):
        t.right(90)
        t.forward(sz)
        sz += 5
    return sz

def draw_second_spiral(t, sz):
    for i in range(50):
        for color in  ["blue","green"]:
            t.color(color)
            t.forward(sz)
            t.right(90)
            t.right(1)
            sz += 3

tess = turtle.Turtle()
tess.pensize(3)
tess.color('blue')
tess.speed(10)
size = 2

#draw_second_spiral(tess, size)
#size = draw_second_spiral(tess, size)

draw_second_spiral(tess, size)

wn.mainloop()


