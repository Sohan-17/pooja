import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)
t.speed(0)
sc = turtle.Screen()
sc.bgcolor("green")

def square():
    for i in range(8):
        t.forward(40)
        t.right(90)
    t.forward(40)

for i in range(8):
    t.penup()
    t.goto(0, 40*i)
    t.pendown()


    for j in range(8):
        if (i+j)%2==0:
            color="black"
        else:
            color="white"


        t.fillcolor(color)
        t.begin_fill()
        square()
        t.end_fill()
