import turtle

screen = turtle.Screen()
screen.bgcolor("Purple") 


star_turtle = turtle.Turtle()
star_turtle.pencolor("Yellow") 
star_turtle.fillcolor("Black")
star_turtle.pensize(5) 
star_turtle.speed(1) 

# Draw the star
star_turtle.begin_fill()
for _ in range(5):
    star_turtle.forward(100) 
    star_turtle.right(144)   
star_turtle.end_fill()


turtle.done()