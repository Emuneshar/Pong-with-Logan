import turtle
import os

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
#window.tracer(0)

# Score variables
leftScore = 0
rightScore = 0

# Paddle A code
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

# Paddle B code
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

# Code for the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx = 0.05
ball.dy = -0.05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player One: 0 Player 2 : 0 ", align="center", font=("Courier", 24, "normal"))

def paddleAUp():
    y = paddleA.ycor()
    y+=20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y+=20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keyboard bindings
window.listen()
window.onkeypress(paddleAUp, "w")

while True:
    window.update()
    



