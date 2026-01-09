import turtle
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Pentagon and Circle")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(2) # Set drawing speed (1 slowest, 10 fastest)

# --- Function to draw a regular polygon (used for the pentagon) ---
def draw_polygon(turt, sides, length):
    for _ in range(sides):
        turt.forward(length)
        turt.left(360 / sides)

# --- Function to draw a circle ---
def draw_circle(turt, radius):
    turt.circle(radius)

# 1. Draw the Pentagon
pen.penup()        # Lift the pen
pen.goto(-100, 50) # Move to a starting position for the pentagon
pen.pendown()      # Put the pen down
pen.color("blue")
pen.begin_fill()
draw_polygon(pen, 5, 100) # Draw a pentagon with side length 100
pen.end_fill()

# 2. Draw the Circle
pen.penup()          # Lift the pen
pen.goto(100, 0)     # Move to a starting position for the circle
pen.pendown()        # Put the pen down
pen.color("red")
pen.begin_fill()
draw_circle(pen, 70) # Draw a circle with radius 70
pen.end_fill()

# Hide the turtle and keep the window open
pen.hideturtle()
turtle.mainloop() # Keeps the window open until manually closed