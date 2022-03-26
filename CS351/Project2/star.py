from turtle import *

import turtle

file = open("turtle_test.txt", "a")

tur = turtle.Turtle()
  

tur.speed(6)
  
tur.getscreen().bgcolor("black")
tur.color("cyan")

tur.penup()
  
tur.goto((-200, 50))
  

tur.pendown()
  

def star(turtle, size):
    if size <= 10:
      file.write(
      return
    else:
        for i in range(5):
            

            turtle.forward(size)
            
            star(turtle, size/3)
  

            turtle.left(216)
  
 
star(tur, 360)
turtle.done()