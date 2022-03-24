# Generated from turtle.g4 by ANTLR 4.9
from antlr4 import *

if __name__ is not None and "." in __name__:
  from .turtleParser import turtleParser
else:
  from turtleParser import turtleParser

# This class defines a complete generic visitor for a parse tree produced by turtleParser.

import turtle
from turtle import Screen
import random as random

tutu = turtle.Turtle()
screen = Screen()

""" def f(x):
    match (x):
      case 0:
        return 'blue'
      case 1:
          return 'white'
      case 2:
        return 'red'
      case _:        
          return 0
 """

#GUI Settings---------------------------

screen.bgcolor('black')
screen.screensize(500,500)
tutu.shape('turtle')
tutu.pencolor('white')
tutu.speed(5)
tutu.pensize(2);



class turtleVisitor(ParseTreeVisitor):
  
  # Visit a parse tree produced by turtleParser#start.
  def visitStart(self, ctx:turtleParser.StartContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by turtleParser#drawLine.
  def visitDrawLine(self, ctx:turtleParser.DrawLineContext):
    
    tutu.pencolor()
    tutu.pendown()
      
    target = int(ctx.whereto.text)
    cursor_position = tutu.pos();

    tutu.forward(target)

    
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


  # Visit a parse tree produced by turtleParser#rotate.
  def visitRotate(self, ctx:turtleParser.RotateContext):
    
    clock = int(ctx.clock.text)
    tutu.lt(clock)
      
    return self.visitChildren(ctx)


  # Visit a parse tree produced by turtleParser#printValues.
  def visitPrintValues(self, ctx:turtleParser.PrintValuesContext):
    return self.visitChildren(ctx)


del turtleParser