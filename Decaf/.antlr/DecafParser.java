// Generated from d:\UVG\5toAno\comp2\Lab00DDC\Decaf\Decaf.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class DecafParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, ID=41, NUM=42, CHAR=43, WS=44, COMMENT=45, LINE_COMMENT=46;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_varDeclaration = 2, RULE_structDeclaration = 3, 
		RULE_varType = 4, RULE_methodDeclaration = 5, RULE_methodType = 6, RULE_parameter = 7, 
		RULE_parameterType = 8, RULE_block = 9, RULE_statement = 10, RULE_expressionOom = 11, 
		RULE_location = 12, RULE_expression = 13, RULE_methodCall = 14, RULE_arg1 = 15, 
		RULE_arg2 = 16, RULE_arg = 17, RULE_rel_op = 18, RULE_eq_op = 19, RULE_arith_op_fifth = 20, 
		RULE_arith_op_fourth = 21, RULE_arith_op_third = 22, RULE_arith_op_second = 23, 
		RULE_arith_op_first = 24, RULE_literal = 25, RULE_int_literal = 26, RULE_char_literal = 27, 
		RULE_bool_literal = 28;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "varDeclaration", "structDeclaration", "varType", 
			"methodDeclaration", "methodType", "parameter", "parameterType", "block", 
			"statement", "expressionOom", "location", "expression", "methodCall", 
			"arg1", "arg2", "arg", "rel_op", "eq_op", "arith_op_fifth", "arith_op_fourth", 
			"arith_op_third", "arith_op_second", "arith_op_first", "literal", "int_literal", 
			"char_literal", "bool_literal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'Program'", "'{'", "'}'", "';'", "'['", "']'", "'struct'", 
			"'int'", "'char'", "'boolean'", "'void'", "'('", "','", "')'", "'if'", 
			"'else'", "'while'", "'return'", "'='", "'.'", "'-'", "'!'", "'<'", "'>'", 
			"'<='", "'>='", "'=='", "'!='", "'*'", "'/'", "'%'", "'<<'", "'>>'", 
			"'+'", "'&&'", "'||'", "'''", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "ID", "NUM", "CHAR", "WS", "COMMENT", "LINE_COMMENT"
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
	public String getGrammarFileName() { return "Decaf.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DecafParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(T__0);
			setState(59);
			match(T__1);
			setState(60);
			match(T__2);
			setState(64);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11))) != 0)) {
				{
				{
				setState(61);
				declaration();
				}
				}
				setState(66);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(67);
			match(T__3);
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

	public static class DeclarationContext extends ParserRuleContext {
		public StructDeclarationContext structDeclaration() {
			return getRuleContext(StructDeclarationContext.class,0);
		}
		public VarDeclarationContext varDeclaration() {
			return getRuleContext(VarDeclarationContext.class,0);
		}
		public MethodDeclarationContext methodDeclaration() {
			return getRuleContext(MethodDeclarationContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(72);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				structDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				varDeclaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(71);
				methodDeclaration();
				}
				break;
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

	public static class VarDeclarationContext extends ParserRuleContext {
		public VarTypeContext varType() {
			return getRuleContext(VarTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public TerminalNode NUM() { return getToken(DecafParser.NUM, 0); }
		public VarDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDeclaration; }
	}

	public final VarDeclarationContext varDeclaration() throws RecognitionException {
		VarDeclarationContext _localctx = new VarDeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_varDeclaration);
		try {
			setState(85);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(74);
				varType();
				setState(75);
				match(ID);
				setState(76);
				match(T__4);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				varType();
				setState(79);
				match(ID);
				setState(80);
				match(T__5);
				setState(81);
				match(NUM);
				setState(82);
				match(T__6);
				setState(83);
				match(T__4);
				}
				break;
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

	public static class StructDeclarationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public List<VarDeclarationContext> varDeclaration() {
			return getRuleContexts(VarDeclarationContext.class);
		}
		public VarDeclarationContext varDeclaration(int i) {
			return getRuleContext(VarDeclarationContext.class,i);
		}
		public StructDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structDeclaration; }
	}

	public final StructDeclarationContext structDeclaration() throws RecognitionException {
		StructDeclarationContext _localctx = new StructDeclarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_structDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(T__7);
			setState(88);
			match(ID);
			setState(89);
			match(T__2);
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11))) != 0)) {
				{
				{
				setState(90);
				varDeclaration();
				}
				}
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(96);
			match(T__3);
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(97);
				match(T__4);
				}
			}

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

	public static class VarTypeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public StructDeclarationContext structDeclaration() {
			return getRuleContext(StructDeclarationContext.class,0);
		}
		public VarTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varType; }
	}

	public final VarTypeContext varType() throws RecognitionException {
		VarTypeContext _localctx = new VarTypeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_varType);
		try {
			setState(107);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(100);
				match(T__8);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(101);
				match(T__9);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(102);
				match(T__10);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(103);
				match(T__7);
				setState(104);
				match(ID);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(105);
				structDeclaration();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(106);
				match(T__11);
				}
				break;
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

	public static class MethodDeclarationContext extends ParserRuleContext {
		public MethodTypeContext methodType() {
			return getRuleContext(MethodTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public MethodDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodDeclaration; }
	}

	public final MethodDeclarationContext methodDeclaration() throws RecognitionException {
		MethodDeclarationContext _localctx = new MethodDeclarationContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_methodDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			methodType();
			setState(110);
			match(ID);
			setState(111);
			match(T__12);
			setState(122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11))) != 0)) {
				{
				{
				setState(112);
				parameter();
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__13) {
					{
					{
					setState(113);
					match(T__13);
					setState(114);
					parameter();
					}
					}
					setState(119);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(125);
			match(T__14);
			setState(126);
			block();
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

	public static class MethodTypeContext extends ParserRuleContext {
		public MethodTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodType; }
	}

	public final MethodTypeContext methodType() throws RecognitionException {
		MethodTypeContext _localctx = new MethodTypeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_methodType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class ParameterContext extends ParserRuleContext {
		public ParameterTypeContext parameterType() {
			return getRuleContext(ParameterTypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_parameter);
		try {
			setState(139);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(130);
				parameterType();
				setState(131);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(133);
				parameterType();
				setState(134);
				match(ID);
				setState(135);
				match(T__5);
				setState(136);
				match(T__6);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(138);
				match(T__11);
				}
				break;
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

	public static class ParameterTypeContext extends ParserRuleContext {
		public ParameterTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterType; }
	}

	public final ParameterTypeContext parameterType() throws RecognitionException {
		ParameterTypeContext _localctx = new ParameterTypeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_parameterType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class BlockContext extends ParserRuleContext {
		public List<VarDeclarationContext> varDeclaration() {
			return getRuleContexts(VarDeclarationContext.class);
		}
		public VarDeclarationContext varDeclaration(int i) {
			return getRuleContext(VarDeclarationContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			match(T__2);
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__11))) != 0)) {
				{
				{
				setState(144);
				varDeclaration();
				}
				}
				setState(149);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(153);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__4) | (1L << T__12) | (1L << T__15) | (1L << T__17) | (1L << T__18) | (1L << T__21) | (1L << T__22) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << ID) | (1L << NUM))) != 0)) {
				{
				{
				setState(150);
				statement();
				}
				}
				setState(155);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(156);
			match(T__3);
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

	public static class StatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public ExpressionOomContext expressionOom() {
			return getRuleContext(ExpressionOomContext.class,0);
		}
		public MethodCallContext methodCall() {
			return getRuleContext(MethodCallContext.class,0);
		}
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_statement);
		int _la;
		try {
			setState(189);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(158);
				match(T__15);
				setState(159);
				match(T__12);
				setState(160);
				expression(0);
				setState(161);
				match(T__14);
				setState(162);
				block();
				setState(165);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__16) {
					{
					setState(163);
					match(T__16);
					setState(164);
					block();
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(167);
				match(T__17);
				setState(168);
				match(T__12);
				setState(169);
				expression(0);
				setState(170);
				match(T__14);
				setState(171);
				block();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(173);
				match(T__18);
				setState(174);
				expressionOom();
				setState(175);
				match(T__4);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(177);
				methodCall();
				setState(178);
				match(T__4);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(180);
				block();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(181);
				location();
				setState(182);
				match(T__19);
				setState(183);
				expression(0);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(186);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__12) | (1L << T__21) | (1L << T__22) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << ID) | (1L << NUM))) != 0)) {
					{
					setState(185);
					expression(0);
					}
				}

				setState(188);
				match(T__4);
				}
				break;
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

	public static class ExpressionOomContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionOomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionOom; }
	}

	public final ExpressionOomContext expressionOom() throws RecognitionException {
		ExpressionOomContext _localctx = new ExpressionOomContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_expressionOom);
		try {
			setState(193);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__12:
			case T__21:
			case T__22:
			case T__37:
			case T__38:
			case T__39:
			case ID:
			case NUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(191);
				expression(0);
				}
				break;
			case T__4:
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

	public static class LocationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public LocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_location; }
	}

	public final LocationContext location() throws RecognitionException {
		LocationContext _localctx = new LocationContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_location);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(195);
				match(ID);
				}
				break;
			case 2:
				{
				setState(196);
				match(ID);
				setState(197);
				match(T__5);
				setState(198);
				expression(0);
				setState(199);
				match(T__6);
				}
				break;
			}
			setState(205);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(203);
				match(T__20);
				setState(204);
				location();
				}
				break;
			}
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

	public static class ExpressionContext extends ParserRuleContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public MethodCallContext methodCall() {
			return getRuleContext(MethodCallContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_fifthContext arith_op_fifth() {
			return getRuleContext(Arith_op_fifthContext.class,0);
		}
		public Arith_op_fourthContext arith_op_fourth() {
			return getRuleContext(Arith_op_fourthContext.class,0);
		}
		public Arith_op_thirdContext arith_op_third() {
			return getRuleContext(Arith_op_thirdContext.class,0);
		}
		public Arith_op_secondContext arith_op_second() {
			return getRuleContext(Arith_op_secondContext.class,0);
		}
		public Arith_op_firstContext arith_op_first() {
			return getRuleContext(Arith_op_firstContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 26;
		enterRecursionRule(_localctx, 26, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(208);
				location();
				}
				break;
			case 2:
				{
				setState(209);
				methodCall();
				}
				break;
			case 3:
				{
				setState(210);
				literal();
				}
				break;
			case 4:
				{
				setState(211);
				match(T__21);
				setState(212);
				expression(8);
				}
				break;
			case 5:
				{
				setState(213);
				match(T__22);
				setState(214);
				expression(7);
				}
				break;
			case 6:
				{
				setState(215);
				match(T__12);
				setState(216);
				expression(0);
				setState(217);
				match(T__14);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(243);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(241);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(221);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(222);
						arith_op_fifth();
						setState(223);
						expression(6);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(225);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(226);
						arith_op_fourth();
						setState(227);
						expression(5);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(229);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(230);
						arith_op_third();
						setState(231);
						expression(4);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(233);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(234);
						arith_op_second();
						setState(235);
						expression(3);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(237);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(238);
						arith_op_first();
						setState(239);
						expression(2);
						}
						break;
					}
					} 
				}
				setState(245);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class MethodCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(DecafParser.ID, 0); }
		public Arg1Context arg1() {
			return getRuleContext(Arg1Context.class,0);
		}
		public MethodCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodCall; }
	}

	public final MethodCallContext methodCall() throws RecognitionException {
		MethodCallContext _localctx = new MethodCallContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_methodCall);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			match(ID);
			setState(247);
			match(T__12);
			setState(248);
			arg1();
			setState(249);
			match(T__14);
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

	public static class Arg1Context extends ParserRuleContext {
		public Arg2Context arg2() {
			return getRuleContext(Arg2Context.class,0);
		}
		public Arg1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg1; }
	}

	public final Arg1Context arg1() throws RecognitionException {
		Arg1Context _localctx = new Arg1Context(_ctx, getState());
		enterRule(_localctx, 30, RULE_arg1);
		try {
			setState(253);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__12:
			case T__21:
			case T__22:
			case T__37:
			case T__38:
			case T__39:
			case ID:
			case NUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(251);
				arg2();
				}
				break;
			case T__14:
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

	public static class Arg2Context extends ParserRuleContext {
		public List<ArgContext> arg() {
			return getRuleContexts(ArgContext.class);
		}
		public ArgContext arg(int i) {
			return getRuleContext(ArgContext.class,i);
		}
		public Arg2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg2; }
	}

	public final Arg2Context arg2() throws RecognitionException {
		Arg2Context _localctx = new Arg2Context(_ctx, getState());
		enterRule(_localctx, 32, RULE_arg2);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(255);
			arg();
			}
			setState(260);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__13) {
				{
				{
				setState(256);
				match(T__13);
				setState(257);
				arg();
				}
				}
				setState(262);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class ArgContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ArgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg; }
	}

	public final ArgContext arg() throws RecognitionException {
		ArgContext _localctx = new ArgContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_arg);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			expression(0);
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

	public static class Rel_opContext extends ParserRuleContext {
		public Rel_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rel_op; }
	}

	public final Rel_opContext rel_op() throws RecognitionException {
		Rel_opContext _localctx = new Rel_opContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_rel_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__23) | (1L << T__24) | (1L << T__25) | (1L << T__26))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Eq_opContext extends ParserRuleContext {
		public Eq_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_eq_op; }
	}

	public final Eq_opContext eq_op() throws RecognitionException {
		Eq_opContext _localctx = new Eq_opContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_eq_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			_la = _input.LA(1);
			if ( !(_la==T__27 || _la==T__28) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Arith_op_fifthContext extends ParserRuleContext {
		public Arith_op_fifthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op_fifth; }
	}

	public final Arith_op_fifthContext arith_op_fifth() throws RecognitionException {
		Arith_op_fifthContext _localctx = new Arith_op_fifthContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_arith_op_fifth);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(269);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Arith_op_fourthContext extends ParserRuleContext {
		public Arith_op_fourthContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op_fourth; }
	}

	public final Arith_op_fourthContext arith_op_fourth() throws RecognitionException {
		Arith_op_fourthContext _localctx = new Arith_op_fourthContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_arith_op_fourth);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			_la = _input.LA(1);
			if ( !(_la==T__21 || _la==T__34) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public static class Arith_op_thirdContext extends ParserRuleContext {
		public Rel_opContext rel_op() {
			return getRuleContext(Rel_opContext.class,0);
		}
		public Eq_opContext eq_op() {
			return getRuleContext(Eq_opContext.class,0);
		}
		public Arith_op_thirdContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op_third; }
	}

	public final Arith_op_thirdContext arith_op_third() throws RecognitionException {
		Arith_op_thirdContext _localctx = new Arith_op_thirdContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_arith_op_third);
		try {
			setState(275);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__23:
			case T__24:
			case T__25:
			case T__26:
				enterOuterAlt(_localctx, 1);
				{
				setState(273);
				rel_op();
				}
				break;
			case T__27:
			case T__28:
				enterOuterAlt(_localctx, 2);
				{
				setState(274);
				eq_op();
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

	public static class Arith_op_secondContext extends ParserRuleContext {
		public Arith_op_secondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op_second; }
	}

	public final Arith_op_secondContext arith_op_second() throws RecognitionException {
		Arith_op_secondContext _localctx = new Arith_op_secondContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_arith_op_second);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			match(T__35);
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

	public static class Arith_op_firstContext extends ParserRuleContext {
		public Arith_op_firstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arith_op_first; }
	}

	public final Arith_op_firstContext arith_op_first() throws RecognitionException {
		Arith_op_firstContext _localctx = new Arith_op_firstContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_arith_op_first);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(279);
			match(T__36);
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

	public static class LiteralContext extends ParserRuleContext {
		public Int_literalContext int_literal() {
			return getRuleContext(Int_literalContext.class,0);
		}
		public Char_literalContext char_literal() {
			return getRuleContext(Char_literalContext.class,0);
		}
		public Bool_literalContext bool_literal() {
			return getRuleContext(Bool_literalContext.class,0);
		}
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_literal);
		try {
			setState(284);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(281);
				int_literal();
				}
				break;
			case T__37:
				enterOuterAlt(_localctx, 2);
				{
				setState(282);
				char_literal();
				}
				break;
			case T__38:
			case T__39:
				enterOuterAlt(_localctx, 3);
				{
				setState(283);
				bool_literal();
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

	public static class Int_literalContext extends ParserRuleContext {
		public TerminalNode NUM() { return getToken(DecafParser.NUM, 0); }
		public Int_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_literal; }
	}

	public final Int_literalContext int_literal() throws RecognitionException {
		Int_literalContext _localctx = new Int_literalContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_int_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			match(NUM);
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

	public static class Char_literalContext extends ParserRuleContext {
		public TerminalNode CHAR() { return getToken(DecafParser.CHAR, 0); }
		public Char_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_char_literal; }
	}

	public final Char_literalContext char_literal() throws RecognitionException {
		Char_literalContext _localctx = new Char_literalContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_char_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			match(T__37);
			setState(289);
			match(CHAR);
			setState(290);
			match(T__37);
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

	public static class Bool_literalContext extends ParserRuleContext {
		public Bool_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_literal; }
	}

	public final Bool_literalContext bool_literal() throws RecognitionException {
		Bool_literalContext _localctx = new Bool_literalContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_bool_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			_la = _input.LA(1);
			if ( !(_la==T__38 || _la==T__39) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 13:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		case 3:
			return precpred(_ctx, 2);
		case 4:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60\u0129\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\3\2\3\2\3\2\3\2\7\2"+
		"A\n\2\f\2\16\2D\13\2\3\2\3\2\3\3\3\3\3\3\5\3K\n\3\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\5\4X\n\4\3\5\3\5\3\5\3\5\7\5^\n\5\f\5\16\5a\13"+
		"\5\3\5\3\5\5\5e\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6n\n\6\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\7\7v\n\7\f\7\16\7y\13\7\7\7{\n\7\f\7\16\7~\13\7\3\7\3\7\3\7"+
		"\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u008e\n\t\3\n\3\n\3\13"+
		"\3\13\7\13\u0094\n\13\f\13\16\13\u0097\13\13\3\13\7\13\u009a\n\13\f\13"+
		"\16\13\u009d\13\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00a8\n\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\5\f\u00bd\n\f\3\f\5\f\u00c0\n\f\3\r\3\r\5\r\u00c4\n\r\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\5\16\u00cc\n\16\3\16\3\16\5\16\u00d0\n\16\3\17\3"+
		"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00de\n\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00f4\n\17\f\17\16\17\u00f7\13\17"+
		"\3\20\3\20\3\20\3\20\3\20\3\21\3\21\5\21\u0100\n\21\3\22\3\22\3\22\7\22"+
		"\u0105\n\22\f\22\16\22\u0108\13\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26"+
		"\3\26\3\27\3\27\3\30\3\30\5\30\u0116\n\30\3\31\3\31\3\32\3\32\3\33\3\33"+
		"\3\33\5\33\u011f\n\33\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\2\3"+
		"\34\37\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:\2"+
		"\t\3\2\13\16\3\2\13\r\3\2\32\35\3\2\36\37\3\2 $\4\2\30\30%%\3\2)*\2\u0136"+
		"\2<\3\2\2\2\4J\3\2\2\2\6W\3\2\2\2\bY\3\2\2\2\nm\3\2\2\2\fo\3\2\2\2\16"+
		"\u0082\3\2\2\2\20\u008d\3\2\2\2\22\u008f\3\2\2\2\24\u0091\3\2\2\2\26\u00bf"+
		"\3\2\2\2\30\u00c3\3\2\2\2\32\u00cb\3\2\2\2\34\u00dd\3\2\2\2\36\u00f8\3"+
		"\2\2\2 \u00ff\3\2\2\2\"\u0101\3\2\2\2$\u0109\3\2\2\2&\u010b\3\2\2\2(\u010d"+
		"\3\2\2\2*\u010f\3\2\2\2,\u0111\3\2\2\2.\u0115\3\2\2\2\60\u0117\3\2\2\2"+
		"\62\u0119\3\2\2\2\64\u011e\3\2\2\2\66\u0120\3\2\2\28\u0122\3\2\2\2:\u0126"+
		"\3\2\2\2<=\7\3\2\2=>\7\4\2\2>B\7\5\2\2?A\5\4\3\2@?\3\2\2\2AD\3\2\2\2B"+
		"@\3\2\2\2BC\3\2\2\2CE\3\2\2\2DB\3\2\2\2EF\7\6\2\2F\3\3\2\2\2GK\5\b\5\2"+
		"HK\5\6\4\2IK\5\f\7\2JG\3\2\2\2JH\3\2\2\2JI\3\2\2\2K\5\3\2\2\2LM\5\n\6"+
		"\2MN\7+\2\2NO\7\7\2\2OX\3\2\2\2PQ\5\n\6\2QR\7+\2\2RS\7\b\2\2ST\7,\2\2"+
		"TU\7\t\2\2UV\7\7\2\2VX\3\2\2\2WL\3\2\2\2WP\3\2\2\2X\7\3\2\2\2YZ\7\n\2"+
		"\2Z[\7+\2\2[_\7\5\2\2\\^\5\6\4\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2"+
		"\2\2`b\3\2\2\2a_\3\2\2\2bd\7\6\2\2ce\7\7\2\2dc\3\2\2\2de\3\2\2\2e\t\3"+
		"\2\2\2fn\7\13\2\2gn\7\f\2\2hn\7\r\2\2ij\7\n\2\2jn\7+\2\2kn\5\b\5\2ln\7"+
		"\16\2\2mf\3\2\2\2mg\3\2\2\2mh\3\2\2\2mi\3\2\2\2mk\3\2\2\2ml\3\2\2\2n\13"+
		"\3\2\2\2op\5\16\b\2pq\7+\2\2q|\7\17\2\2rw\5\20\t\2st\7\20\2\2tv\5\20\t"+
		"\2us\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x{\3\2\2\2yw\3\2\2\2zr\3\2\2"+
		"\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\177\3\2\2\2~|\3\2\2\2\177\u0080\7\21"+
		"\2\2\u0080\u0081\5\24\13\2\u0081\r\3\2\2\2\u0082\u0083\t\2\2\2\u0083\17"+
		"\3\2\2\2\u0084\u0085\5\22\n\2\u0085\u0086\7+\2\2\u0086\u008e\3\2\2\2\u0087"+
		"\u0088\5\22\n\2\u0088\u0089\7+\2\2\u0089\u008a\7\b\2\2\u008a\u008b\7\t"+
		"\2\2\u008b\u008e\3\2\2\2\u008c\u008e\7\16\2\2\u008d\u0084\3\2\2\2\u008d"+
		"\u0087\3\2\2\2\u008d\u008c\3\2\2\2\u008e\21\3\2\2\2\u008f\u0090\t\3\2"+
		"\2\u0090\23\3\2\2\2\u0091\u0095\7\5\2\2\u0092\u0094\5\6\4\2\u0093\u0092"+
		"\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096"+
		"\u009b\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009a\5\26\f\2\u0099\u0098\3"+
		"\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c"+
		"\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\7\6\2\2\u009f\25\3\2\2"+
		"\2\u00a0\u00a1\7\22\2\2\u00a1\u00a2\7\17\2\2\u00a2\u00a3\5\34\17\2\u00a3"+
		"\u00a4\7\21\2\2\u00a4\u00a7\5\24\13\2\u00a5\u00a6\7\23\2\2\u00a6\u00a8"+
		"\5\24\13\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00c0\3\2\2\2"+
		"\u00a9\u00aa\7\24\2\2\u00aa\u00ab\7\17\2\2\u00ab\u00ac\5\34\17\2\u00ac"+
		"\u00ad\7\21\2\2\u00ad\u00ae\5\24\13\2\u00ae\u00c0\3\2\2\2\u00af\u00b0"+
		"\7\25\2\2\u00b0\u00b1\5\30\r\2\u00b1\u00b2\7\7\2\2\u00b2\u00c0\3\2\2\2"+
		"\u00b3\u00b4\5\36\20\2\u00b4\u00b5\7\7\2\2\u00b5\u00c0\3\2\2\2\u00b6\u00c0"+
		"\5\24\13\2\u00b7\u00b8\5\32\16\2\u00b8\u00b9\7\26\2\2\u00b9\u00ba\5\34"+
		"\17\2\u00ba\u00c0\3\2\2\2\u00bb\u00bd\5\34\17\2\u00bc\u00bb\3\2\2\2\u00bc"+
		"\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0\7\7\2\2\u00bf\u00a0\3\2"+
		"\2\2\u00bf\u00a9\3\2\2\2\u00bf\u00af\3\2\2\2\u00bf\u00b3\3\2\2\2\u00bf"+
		"\u00b6\3\2\2\2\u00bf\u00b7\3\2\2\2\u00bf\u00bc\3\2\2\2\u00c0\27\3\2\2"+
		"\2\u00c1\u00c4\5\34\17\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3"+
		"\u00c2\3\2\2\2\u00c4\31\3\2\2\2\u00c5\u00cc\7+\2\2\u00c6\u00c7\7+\2\2"+
		"\u00c7\u00c8\7\b\2\2\u00c8\u00c9\5\34\17\2\u00c9\u00ca\7\t\2\2\u00ca\u00cc"+
		"\3\2\2\2\u00cb\u00c5\3\2\2\2\u00cb\u00c6\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd"+
		"\u00ce\7\27\2\2\u00ce\u00d0\5\32\16\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0"+
		"\3\2\2\2\u00d0\33\3\2\2\2\u00d1\u00d2\b\17\1\2\u00d2\u00de\5\32\16\2\u00d3"+
		"\u00de\5\36\20\2\u00d4\u00de\5\64\33\2\u00d5\u00d6\7\30\2\2\u00d6\u00de"+
		"\5\34\17\n\u00d7\u00d8\7\31\2\2\u00d8\u00de\5\34\17\t\u00d9\u00da\7\17"+
		"\2\2\u00da\u00db\5\34\17\2\u00db\u00dc\7\21\2\2\u00dc\u00de\3\2\2\2\u00dd"+
		"\u00d1\3\2\2\2\u00dd\u00d3\3\2\2\2\u00dd\u00d4\3\2\2\2\u00dd\u00d5\3\2"+
		"\2\2\u00dd\u00d7\3\2\2\2\u00dd\u00d9\3\2\2\2\u00de\u00f5\3\2\2\2\u00df"+
		"\u00e0\f\7\2\2\u00e0\u00e1\5*\26\2\u00e1\u00e2\5\34\17\b\u00e2\u00f4\3"+
		"\2\2\2\u00e3\u00e4\f\6\2\2\u00e4\u00e5\5,\27\2\u00e5\u00e6\5\34\17\7\u00e6"+
		"\u00f4\3\2\2\2\u00e7\u00e8\f\5\2\2\u00e8\u00e9\5.\30\2\u00e9\u00ea\5\34"+
		"\17\6\u00ea\u00f4\3\2\2\2\u00eb\u00ec\f\4\2\2\u00ec\u00ed\5\60\31\2\u00ed"+
		"\u00ee\5\34\17\5\u00ee\u00f4\3\2\2\2\u00ef\u00f0\f\3\2\2\u00f0\u00f1\5"+
		"\62\32\2\u00f1\u00f2\5\34\17\4\u00f2\u00f4\3\2\2\2\u00f3\u00df\3\2\2\2"+
		"\u00f3\u00e3\3\2\2\2\u00f3\u00e7\3\2\2\2\u00f3\u00eb\3\2\2\2\u00f3\u00ef"+
		"\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6"+
		"\35\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9\7+\2\2\u00f9\u00fa\7\17\2"+
		"\2\u00fa\u00fb\5 \21\2\u00fb\u00fc\7\21\2\2\u00fc\37\3\2\2\2\u00fd\u0100"+
		"\5\"\22\2\u00fe\u0100\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u00fe\3\2\2\2"+
		"\u0100!\3\2\2\2\u0101\u0106\5$\23\2\u0102\u0103\7\20\2\2\u0103\u0105\5"+
		"$\23\2\u0104\u0102\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106"+
		"\u0107\3\2\2\2\u0107#\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u010a\5\34\17"+
		"\2\u010a%\3\2\2\2\u010b\u010c\t\4\2\2\u010c\'\3\2\2\2\u010d\u010e\t\5"+
		"\2\2\u010e)\3\2\2\2\u010f\u0110\t\6\2\2\u0110+\3\2\2\2\u0111\u0112\t\7"+
		"\2\2\u0112-\3\2\2\2\u0113\u0116\5&\24\2\u0114\u0116\5(\25\2\u0115\u0113"+
		"\3\2\2\2\u0115\u0114\3\2\2\2\u0116/\3\2\2\2\u0117\u0118\7&\2\2\u0118\61"+
		"\3\2\2\2\u0119\u011a\7\'\2\2\u011a\63\3\2\2\2\u011b\u011f\5\66\34\2\u011c"+
		"\u011f\58\35\2\u011d\u011f\5:\36\2\u011e\u011b\3\2\2\2\u011e\u011c\3\2"+
		"\2\2\u011e\u011d\3\2\2\2\u011f\65\3\2\2\2\u0120\u0121\7,\2\2\u0121\67"+
		"\3\2\2\2\u0122\u0123\7(\2\2\u0123\u0124\7-\2\2\u0124\u0125\7(\2\2\u0125"+
		"9\3\2\2\2\u0126\u0127\t\b\2\2\u0127;\3\2\2\2\32BJW_dmw|\u008d\u0095\u009b"+
		"\u00a7\u00bc\u00bf\u00c3\u00cb\u00cf\u00dd\u00f3\u00f5\u00ff\u0106\u0115"+
		"\u011e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}