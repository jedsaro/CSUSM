
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

#GUI Settings---------------------------

class turtleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by turtleParser#start.
    def visitStart(self, ctx:turtleParser.StartContext):
      return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawLine.
    def visitDrawLine(self, ctx:turtleParser.DrawLineContext): #G01
      
      xcord = float(ctx.x_cord.text)
      
      ycord = float(ctx.y_cord.text)
      
      print(xcord,ycord)
      
      tutu.goto(xcord,ycord)
      
      return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawCircle.
    def visitDrawCircle(self, ctx:turtleParser.DrawCircleContext): #G02
      
      radius = int(ctx.radius.text)
      extent = int(ctx.extent.text)
      
      tutu.circle(radius,extent)

      return self.visitChildren(ctx)

    # Visit a parse tree produced by turtleParser#removepen.
    def visitRemovepen(self, ctx:turtleParser.RemovepenContext): #M05
      
      tutu.penup()
      
      return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#addpen.
    def visitAddpen(self, ctx:turtleParser.AddpenContext): #M03
      
      tutu.pendown();
      
      return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#rotate.
    def visitRotate(self, ctx:turtleParser.RotateContext): #G68
      
      clock = int(ctx.clock.text)
      tutu.right(clock)
      
      return self.visitChildren(ctx)

del turtleParser