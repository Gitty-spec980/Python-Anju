import turtle
turtle.Screen().bgcolor('pink')
t=turtle.Screen()


turtle.title("First program using Tutles")
t=turtle.Turtle()
t.pensize(5)
t.speed(8)
t.pencolor('purple')
t.left(90)
t.fillcolor('yellow')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()
#Making a triangle starting from here
t.penup()
t.goto(-100,0)
t.pendown()
t.right(90)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.hideturtle()
turtle.done()



