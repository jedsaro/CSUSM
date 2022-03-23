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


    # Visit a parse tree produced by turtleParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:turtleParser.DrawlineExprContext):
        target_x    = int(ctx.x_cord.text)
        target_y    = int(ctx.y_cord.text)
        cur_pos     = tutu.pos()
        
        

        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#printlineExpr.
    def visitPrintlineExpr(self, ctx:turtleParser.PrintlineExprContext):
        print(f"Draw line to x={ctx.x_cord.text} y={ctx.y_cord.text}")
        return self.visitChildren(ctx)



del turtleParser