# Generated from turtle.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write(";\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\6\7)\n")
        buf.write("\7\r\7\16\7*\3\7\3\7\6\7/\n\7\r\7\16\7\60\5\7\63\n\7\3")
        buf.write("\b\6\b\66\n\b\r\b\16\b\67\3\b\3\b\2\2\t\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\3\2\3\5\2\13\f\17\17\"\"\2>\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\25\3\2\2\2\7\31")
        buf.write("\3\2\2\2\t\35\3\2\2\2\13!\3\2\2\2\r(\3\2\2\2\17\65\3\2")
        buf.write("\2\2\21\22\7I\2\2\22\23\7\62\2\2\23\24\7\63\2\2\24\4\3")
        buf.write("\2\2\2\25\26\7I\2\2\26\27\7\62\2\2\27\30\7\64\2\2\30\6")
        buf.write("\3\2\2\2\31\32\7I\2\2\32\33\7\64\2\2\33\34\7:\2\2\34\b")
        buf.write("\3\2\2\2\35\36\7I\2\2\36\37\78\2\2\37 \7:\2\2 \n\3\2\2")
        buf.write("\2!\"\7r\2\2\"#\7t\2\2#$\7k\2\2$%\7p\2\2%&\7v\2\2&\f\3")
        buf.write("\2\2\2\')\4\62;\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2")
        buf.write("\2\2+\62\3\2\2\2,.\7\60\2\2-/\4\62;\2.-\3\2\2\2/\60\3")
        buf.write("\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\63\3\2\2\2\62,\3\2")
        buf.write("\2\2\62\63\3\2\2\2\63\16\3\2\2\2\64\66\t\2\2\2\65\64\3")
        buf.write("\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\289\3\2\2")
        buf.write("\29:\b\b\2\2:\20\3\2\2\2\7\2*\60\62\67\3\b\2\2")
        return buf.getvalue()


class turtleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    NUMBER = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'G01'", "'G02'", "'G28'", "'G68'", "'print'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NUMBER", "WS" ]

    grammarFileName = "turtle.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


