# Generated from turtle.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .turtleParser import turtleParser
else:
    from turtleParser import turtleParser

# This class defines a complete listener for a parse tree produced by turtleParser.
class turtleListener(ParseTreeListener):

    # Enter a parse tree produced by turtleParser#start.
    def enterStart(self, ctx:turtleParser.StartContext):
        pass

    # Exit a parse tree produced by turtleParser#start.
    def exitStart(self, ctx:turtleParser.StartContext):
        pass


    # Enter a parse tree produced by turtleParser#drawLine.
    def enterDrawLine(self, ctx:turtleParser.DrawLineContext):
        pass

    # Exit a parse tree produced by turtleParser#drawLine.
    def exitDrawLine(self, ctx:turtleParser.DrawLineContext):
        pass


    # Enter a parse tree produced by turtleParser#drawCircle.
    def enterDrawCircle(self, ctx:turtleParser.DrawCircleContext):
        pass

    # Exit a parse tree produced by turtleParser#drawCircle.
    def exitDrawCircle(self, ctx:turtleParser.DrawCircleContext):
        pass


    # Enter a parse tree produced by turtleParser#returnHome.
    def enterReturnHome(self, ctx:turtleParser.ReturnHomeContext):
        pass

    # Exit a parse tree produced by turtleParser#returnHome.
    def exitReturnHome(self, ctx:turtleParser.ReturnHomeContext):
        pass


    # Enter a parse tree produced by turtleParser#removepen.
    def enterRemovepen(self, ctx:turtleParser.RemovepenContext):
        pass

    # Exit a parse tree produced by turtleParser#removepen.
    def exitRemovepen(self, ctx:turtleParser.RemovepenContext):
        pass


    # Enter a parse tree produced by turtleParser#addpen.
    def enterAddpen(self, ctx:turtleParser.AddpenContext):
        pass

    # Exit a parse tree produced by turtleParser#addpen.
    def exitAddpen(self, ctx:turtleParser.AddpenContext):
        pass


    # Enter a parse tree produced by turtleParser#rotate.
    def enterRotate(self, ctx:turtleParser.RotateContext):
        pass

    # Exit a parse tree produced by turtleParser#rotate.
    def exitRotate(self, ctx:turtleParser.RotateContext):
        pass


    # Enter a parse tree produced by turtleParser#colorFill.
    def enterColorFill(self, ctx:turtleParser.ColorFillContext):
        pass

    # Exit a parse tree produced by turtleParser#colorFill.
    def exitColorFill(self, ctx:turtleParser.ColorFillContext):
        pass



del turtleParser