# importing the module
import turtle
#making a turtle object of Turtle class for drawing
trtl = turtle.Turtle()
# making a canvas for drawing
screen=turtle.Screen()
#choosing the screen size
screen.setup(600,600)
screen.bgcolor('black')
trtl.pencolor('yellow') 
#choosing the size of pen nib
trtl.pensize(5)
trtl.speed(1)


for i in range(4):
      trtl.forward(100)
      trtl.right(90)

trtl.penup()
trtl.setpos(-120,100)
trtl.pendown()
trtl.pencolor('green')
trtl.penup()
trtl.ht()
