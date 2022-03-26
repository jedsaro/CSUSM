# Generated from turtle.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("F\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\t\5\t\61\n\t\3\t\6\t\64\n\t\r\t")
        buf.write("\16\t\65\3\t\3\t\6\t:\n\t\r\t\16\t;\5\t>\n\t\3\n\6\nA")
        buf.write("\n\n\r\n\16\nB\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\3\2\3\5\2\13\f\17\17\"\"\2J\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25")
        buf.write("\3\2\2\2\5\31\3\2\2\2\7\35\3\2\2\2\t!\3\2\2\2\13%\3\2")
        buf.write("\2\2\r)\3\2\2\2\17-\3\2\2\2\21\60\3\2\2\2\23@\3\2\2\2")
        buf.write("\25\26\7I\2\2\26\27\7\62\2\2\27\30\7\63\2\2\30\4\3\2\2")
        buf.write("\2\31\32\7I\2\2\32\33\7\62\2\2\33\34\7\64\2\2\34\6\3\2")
        buf.write("\2\2\35\36\7I\2\2\36\37\7\64\2\2\37 \7:\2\2 \b\3\2\2\2")
        buf.write("!\"\7O\2\2\"#\7\62\2\2#$\7\67\2\2$\n\3\2\2\2%&\7O\2\2")
        buf.write("&\'\7\62\2\2\'(\7\65\2\2(\f\3\2\2\2)*\7I\2\2*+\78\2\2")
        buf.write("+,\7:\2\2,\16\3\2\2\2-.\7\\\2\2.\20\3\2\2\2/\61\7/\2\2")
        buf.write("\60/\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62\64\4\62;\2")
        buf.write("\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2")
        buf.write("\2\66=\3\2\2\2\679\7\60\2\28:\4\62;\298\3\2\2\2:;\3\2")
        buf.write("\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=\67\3\2\2\2=>\3\2\2")
        buf.write("\2>\22\3\2\2\2?A\t\2\2\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2")
        buf.write("BC\3\2\2\2CD\3\2\2\2DE\b\n\2\2E\24\3\2\2\2\b\2\60\65;")
        buf.write("=B\3\b\2\2")
        return buf.getvalue()


class turtleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    NUMBER = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'G01'", "'G02'", "'G28'", "'M05'", "'M03'", "'G68'", "'Z'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "NUMBER", "WS" ]

    grammarFileName = "turtle.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


