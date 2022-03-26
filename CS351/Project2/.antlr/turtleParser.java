// Generated from c:\Users\Jedsa\Desktop\Projects\CSUSM\CS351\Project2\turtle.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class turtleParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, NUMBER=8, WS=9;
	public static final int
		RULE_start = 0, RULE_expr = 1;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'G01'", "'G02'", "'G28'", "'M05'", "'M03'", "'G68'", "'Z'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "NUMBER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "turtle.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public turtleParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		try {
			setState(6);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case T__1:
			case T__2:
			case T__3:
			case T__4:
			case T__5:
			case T__6:
				enterOuterAlt(_localctx, 1);
				{
				setState(4);
				expr();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ReturnHomeContext extends ExprContext {
		public ReturnHomeContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class RotateContext extends ExprContext {
		public Token clock;
		public TerminalNode NUMBER() { return getToken(turtleParser.NUMBER, 0); }
		public RotateContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class DrawCircleContext extends ExprContext {
		public Token radius;
		public Token extent;
		public List<TerminalNode> NUMBER() { return getTokens(turtleParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(turtleParser.NUMBER, i);
		}
		public DrawCircleContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class RemovepenContext extends ExprContext {
		public RemovepenContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ColorFillContext extends ExprContext {
		public Token logic;
		public TerminalNode NUMBER() { return getToken(turtleParser.NUMBER, 0); }
		public ColorFillContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class DrawLineContext extends ExprContext {
		public Token x_cord;
		public Token y_cord;
		public List<TerminalNode> NUMBER() { return getTokens(turtleParser.NUMBER); }
		public TerminalNode NUMBER(int i) {
			return getToken(turtleParser.NUMBER, i);
		}
		public DrawLineContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class AddpenContext extends ExprContext {
		public AddpenContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr);
		try {
			setState(21);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new DrawLineContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(8);
				match(T__0);
				setState(9);
				((DrawLineContext)_localctx).x_cord = match(NUMBER);
				setState(10);
				((DrawLineContext)_localctx).y_cord = match(NUMBER);
				}
				break;
			case T__1:
				_localctx = new DrawCircleContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(11);
				match(T__1);
				setState(12);
				((DrawCircleContext)_localctx).radius = match(NUMBER);
				setState(13);
				((DrawCircleContext)_localctx).extent = match(NUMBER);
				}
				break;
			case T__2:
				_localctx = new ReturnHomeContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(14);
				match(T__2);
				}
				break;
			case T__3:
				_localctx = new RemovepenContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(15);
				match(T__3);
				}
				break;
			case T__4:
				_localctx = new AddpenContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(16);
				match(T__4);
				}
				break;
			case T__5:
				_localctx = new RotateContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(17);
				match(T__5);
				setState(18);
				((RotateContext)_localctx).clock = match(NUMBER);
				}
				break;
			case T__6:
				_localctx = new ColorFillContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(19);
				match(T__6);
				setState(20);
				((ColorFillContext)_localctx).logic = match(NUMBER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13\32\4\2\t\2\4\3"+
		"\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\5\3\30\n\3\3\3\2\2\4\2\4\2\2\2\36\2\b\3\2\2\2\4\27\3\2\2\2\6\t\5"+
		"\4\3\2\7\t\3\2\2\2\b\6\3\2\2\2\b\7\3\2\2\2\t\3\3\2\2\2\n\13\7\3\2\2\13"+
		"\f\7\n\2\2\f\30\7\n\2\2\r\16\7\4\2\2\16\17\7\n\2\2\17\30\7\n\2\2\20\30"+
		"\7\5\2\2\21\30\7\6\2\2\22\30\7\7\2\2\23\24\7\b\2\2\24\30\7\n\2\2\25\26"+
		"\7\t\2\2\26\30\7\n\2\2\27\n\3\2\2\2\27\r\3\2\2\2\27\20\3\2\2\2\27\21\3"+
		"\2\2\2\27\22\3\2\2\2\27\23\3\2\2\2\27\25\3\2\2\2\30\5\3\2\2\2\4\b\27";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}