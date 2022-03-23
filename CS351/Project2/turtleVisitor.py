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

class turtleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by turtleParser#start.
    def visitStart(self, ctx:turtleParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawLine.
    def visitDrawLine(self, ctx:turtleParser.DrawLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawCircle.
    def visitDrawCircle(self, ctx:turtleParser.DrawCircleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#returnHome.
    def visitReturnHome(self, ctx:turtleParser.ReturnHomeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#printValues.
    def visitPrintValues(self, ctx:turtleParser.PrintValuesContext):
        return self.visitChildren(ctx)



del turtleParser