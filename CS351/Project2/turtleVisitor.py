# Generated from turtle.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .turtleParser import turtleParser
else:
    from turtleParser import turtleParser

# This class defines a complete generic visitor for a parse tree produced by turtleParser.

import random, math
from turtle import Screen
import turtle as tutu

screen = Screen()

#GUI Settings---------------------------

screen.bgcolor('black')
screen.screensize(500,500)
tutu.shape('turtle')
tutu.speed(10)
tutu.pensize(2)
class turtleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by turtleParser#start.
    def visitStart(self, ctx:turtleParser.StartContext):
      return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawLine.
    def visitDrawLine(self, ctx:turtleParser.DrawLineContext): #G01
      xcord = float(ctx.x_cord.text)
      ycord = float(ctx.x_cord.text)
      
      c = math.hypot(xcord,ycord)
      
      tutu.forward(c)
      
      return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawCircle.
    def visitDrawCircle(self, ctx:turtleParser.DrawCircleContext): #G02
      
      tutu.colormode(255)
      
      R=random.randint(0,255)
      G=random.randint(0,255)
      B=random.randint(0,255)
      
      tutu.pencolor(R,G,B)
      
      radius = int(ctx.radius.text)
      extent = int(ctx.extent.text)
      
      tutu.circle(radius,extent)

      return self.visitChildren(ctx)

    # Visit a parse tree produced by turtleParser#returnHome.
    def visitReturnHome(self, ctx:turtleParser.ReturnHomeContext): #G28
      
      tutu.penup()
      tutu.home()
      
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

    # Visit a parse tree produced by turtleParser#printValues.
    def visitPrintValues(self, ctx:turtleParser.PrintValuesContext):
      return self.visitChildren(ctx)



del turtleParser