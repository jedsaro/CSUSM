import turtle

file = open('testing.txt', 'a')

# initialise turtle instance
stars = turtle.Turtle()
  
# increases the speed of turtle
stars.speed(10)
  
# to change the background color
stars.getscreen().bgcolor("black")
stars.color("red")
  
# stop drawing
stars.penup()
file.write("M05\n")

  
# move the turtle
stars.goto((-200, 50))
file.write("G01 -200, 50\n")
  
# start drawing
stars.pendown()
file.write("M03\n")


# function to draw stars
def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            # moving turtle forward
            turtle.forward(size)
            file.write(f"G01 {turtle.xcor()} {turtle.ycor()}\n")
    
            star(turtle, size/3)
  
            # moving turtle left
            turtle.left(216)
            file.write("G68 216\n")
  
  
# calling the star function
star(stars, 360)

turtle.done()

