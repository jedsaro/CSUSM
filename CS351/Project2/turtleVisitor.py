# Generated from turtle.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .turtleParser import turtleParser
else:
    from turtleParser import turtleParser

# This class defines a complete generic visitor for a parse tree produced by turtleParser.

import turtle
from turtle import Screen

tutu = turtle.Turtle()
screen = Screen()

#GUI Settings==

screen.bgcolor('black')
screen.screensize(500,500)
tutu.shape('turtle')
tutu.pencolor('white')
tutu.speed(3)
tutu.pensize(2);

class turtleVisitor(ParseTreeVisitor):
  
  
  

    # Visit a parse tree produced by turtleParser#start.
    def visitStart(self, ctx:turtleParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawLine.
    def visitDrawLine(self, ctx:turtleParser.DrawLineContext):
      target_x    = int(ctx.x_cord.text)
      target_y    = int(ctx.y_cord.text)
      direction   = int(ctx.direction.text)
      cursor_position    = tutu.pos();
      
      tutu.pos(direction)
      
      if target_x > cursor_position[0]:
          tutu.right( target_x - cursor_position[0])
      else:
        tutu.left( cursor_position[0] - target_x)

      if target_y > cursor_position[1]:
        tutu.forward( target_y - cursor_position[1])
      else:
        tutu.backward( cursor_position[1] - target_y)
      
      
      return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawCircle.
    def visitDrawCircle(self, ctx:turtleParser.DrawCircleContext):
      
      radius = int(ctx.radius.text)
      extent = int(ctx.extent.text)
        
      tutu.circle(radius,extent)
        
      return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#returnHome.
    def visitReturnHome(self, ctx:turtleParser.ReturnHomeContext):
      tutu.penup()
      tutu.home()
      return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#printValues.
    def visitPrintValues(self, ctx:turtleParser.PrintValuesContext):
        return self.visitChildren(ctx)



del turtleParser