import turtle as t
from turtle import Screen
import random

screen = Screen()

screen.bgcolor('black')
screen.screensize(500,500)

file = open("turtle_test.txt", "a")

t.colormode(255)
t.speed(0)
t.pensize(1)

for i in range (120) :
    t.circle(100)
    file.write("G02 100 360\n")
    t.right(3)
    file.write("G68 3\n")
