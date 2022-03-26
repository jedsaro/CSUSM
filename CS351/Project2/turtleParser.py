# Generated from turtle.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\32\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\3\2")
        buf.write("\2\4\2\4\2\2\2\36\2\b\3\2\2\2\4\27\3\2\2\2\6\t\5\4\3\2")
        buf.write("\7\t\3\2\2\2\b\6\3\2\2\2\b\7\3\2\2\2\t\3\3\2\2\2\n\13")
        buf.write("\7\3\2\2\13\f\7\n\2\2\f\30\7\n\2\2\r\16\7\4\2\2\16\17")
        buf.write("\7\n\2\2\17\30\7\n\2\2\20\30\7\5\2\2\21\30\7\6\2\2\22")
        buf.write("\30\7\7\2\2\23\24\7\b\2\2\24\30\7\n\2\2\25\26\7\t\2\2")
        buf.write("\26\30\7\n\2\2\27\n\3\2\2\2\27\r\3\2\2\2\27\20\3\2\2\2")
        buf.write("\27\21\3\2\2\2\27\22\3\2\2\2\27\23\3\2\2\2\27\25\3\2\2")
        buf.write("\2\30\5\3\2\2\2\4\b\27")
        return buf.getvalue()


class turtleParser ( Parser ):

    grammarFileName = "turtle.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'G01'", "'G02'", "'G28'", "'M05'", "'M03'", 
                     "'G68'", "'Z'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    NUMBER=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(turtleParser.ExprContext,0)


        def getRuleIndex(self):
            return turtleParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = turtleParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [turtleParser.T__0, turtleParser.T__1, turtleParser.T__2, turtleParser.T__3, turtleParser.T__4, turtleParser.T__5, turtleParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [turtleParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return turtleParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReturnHomeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnHome" ):
                listener.enterReturnHome(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnHome" ):
                listener.exitReturnHome(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnHome" ):
                return visitor.visitReturnHome(self)
            else:
                return visitor.visitChildren(self)


    class RotateContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.clock = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(turtleParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRotate" ):
                listener.enterRotate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRotate" ):
                listener.exitRotate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRotate" ):
                return visitor.visitRotate(self)
            else:
                return visitor.visitChildren(self)


    class DrawCircleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.radius = None # Token
            self.extent = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(turtleParser.NUMBER)
            else:
                return self.getToken(turtleParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawCircle" ):
                listener.enterDrawCircle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawCircle" ):
                listener.exitDrawCircle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawCircle" ):
                return visitor.visitDrawCircle(self)
            else:
                return visitor.visitChildren(self)


    class RemovepenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemovepen" ):
                listener.enterRemovepen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemovepen" ):
                listener.exitRemovepen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemovepen" ):
                return visitor.visitRemovepen(self)
            else:
                return visitor.visitChildren(self)


    class ColorFillContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.logic = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(turtleParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColorFill" ):
                listener.enterColorFill(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColorFill" ):
                listener.exitColorFill(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColorFill" ):
                return visitor.visitColorFill(self)
            else:
                return visitor.visitChildren(self)


    class DrawLineContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(turtleParser.NUMBER)
            else:
                return self.getToken(turtleParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawLine" ):
                listener.enterDrawLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawLine" ):
                listener.exitDrawLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawLine" ):
                return visitor.visitDrawLine(self)
            else:
                return visitor.visitChildren(self)


    class AddpenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddpen" ):
                listener.enterAddpen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddpen" ):
                listener.exitAddpen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddpen" ):
                return visitor.visitAddpen(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = turtleParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [turtleParser.T__0]:
                localctx = turtleParser.DrawLineContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(turtleParser.T__0)
                self.state = 9
                localctx.x_cord = self.match(turtleParser.NUMBER)
                self.state = 10
                localctx.y_cord = self.match(turtleParser.NUMBER)
                pass
            elif token in [turtleParser.T__1]:
                localctx = turtleParser.DrawCircleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(turtleParser.T__1)
                self.state = 12
                localctx.radius = self.match(turtleParser.NUMBER)
                self.state = 13
                localctx.extent = self.match(turtleParser.NUMBER)
                pass
            elif token in [turtleParser.T__2]:
                localctx = turtleParser.ReturnHomeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(turtleParser.T__2)
                pass
            elif token in [turtleParser.T__3]:
                localctx = turtleParser.RemovepenContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 15
                self.match(turtleParser.T__3)
                pass
            elif token in [turtleParser.T__4]:
                localctx = turtleParser.AddpenContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 16
                self.match(turtleParser.T__4)
                pass
            elif token in [turtleParser.T__5]:
                localctx = turtleParser.RotateContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 17
                self.match(turtleParser.T__5)
                self.state = 18
                localctx.clock = self.match(turtleParser.NUMBER)
                pass
            elif token in [turtleParser.T__6]:
                localctx = turtleParser.ColorFillContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 19
                self.match(turtleParser.T__6)
                self.state = 20
                localctx.logic = self.match(turtleParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





