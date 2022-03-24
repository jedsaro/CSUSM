# Generated from turtle.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("G\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\6\t\65\n\t\r")
        buf.write("\t\16\t\66\3\t\3\t\6\t;\n\t\r\t\16\t<\5\t?\n\t\3\n\6\n")
        buf.write("B\n\n\r\n\16\nC\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\3\2\3\5\2\13\f\17\17\"\"\2J\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3")
        buf.write("\25\3\2\2\2\5\31\3\2\2\2\7\35\3\2\2\2\t!\3\2\2\2\13%\3")
        buf.write("\2\2\2\r)\3\2\2\2\17-\3\2\2\2\21\64\3\2\2\2\23A\3\2\2")
        buf.write("\2\25\26\7I\2\2\26\27\7\62\2\2\27\30\7\63\2\2\30\4\3\2")
        buf.write("\2\2\31\32\7I\2\2\32\33\7\62\2\2\33\34\7\64\2\2\34\6\3")
        buf.write("\2\2\2\35\36\7I\2\2\36\37\7\64\2\2\37 \7:\2\2 \b\3\2\2")
        buf.write("\2!\"\7O\2\2\"#\7\62\2\2#$\7\67\2\2$\n\3\2\2\2%&\7O\2")
        buf.write("\2&\'\7\62\2\2\'(\7\65\2\2(\f\3\2\2\2)*\7I\2\2*+\78\2")
        buf.write("\2+,\7:\2\2,\16\3\2\2\2-.\7r\2\2./\7t\2\2/\60\7k\2\2\60")
        buf.write("\61\7p\2\2\61\62\7v\2\2\62\20\3\2\2\2\63\65\4\62;\2\64")
        buf.write("\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2")
        buf.write("\67>\3\2\2\28:\7\60\2\29;\4\62;\2:9\3\2\2\2;<\3\2\2\2")
        buf.write("<:\3\2\2\2<=\3\2\2\2=?\3\2\2\2>8\3\2\2\2>?\3\2\2\2?\22")
        buf.write("\3\2\2\2@B\t\2\2\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2")
        buf.write("\2\2DE\3\2\2\2EF\b\n\2\2F\24\3\2\2\2\7\2\66<>C\3\b\2\2")
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
            "'G01'", "'G02'", "'G28'", "'M05'", "'M03'", "'G68'", "'print'" ]

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


