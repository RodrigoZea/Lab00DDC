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
		ID=39, NUM=40, CHAR=41, WS=42, COMMENT=43, LINE_COMMENT=44;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_varDeclaration = 2, RULE_structDeclaration = 3, 
		RULE_varType = 4, RULE_methodDeclaration = 5, RULE_methodType = 6, RULE_parameter = 7, 
		RULE_parameterType = 8, RULE_block = 9, RULE_statement = 10, RULE_expressionOom = 11, 
		RULE_location = 12, RULE_expression = 13, RULE_methodCall = 14, RULE_rel_op = 15, 
		RULE_eq_op = 16, RULE_arith_op_fifth = 17, RULE_arith_op_fourth = 18, 
		RULE_arith_op_third = 19, RULE_arith_op_second = 20, RULE_arith_op_first = 21, 
		RULE_literal = 22, RULE_int_literal = 23, RULE_char_literal = 24, RULE_bool_literal = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "varDeclaration", "structDeclaration", "varType", 
			"methodDeclaration", "methodType", "parameter", "parameterType", "block", 
			"statement", "expressionOom", "location", "expression", "methodCall", 
			"rel_op", "eq_op", "arith_op_fifth", "arith_op_fourth", "arith_op_third", 
			"arith_op_second", "arith_op_first", "literal", "int_literal", "char_literal", 
			"bool_literal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'Program'", "'{'", "'}'", "';'", "'['", "']'", "'struct'", 
			"'int'", "'char'", "'boolean'", "'('", "','", "')'", "'void'", "'if'", 
			"'else'", "'while'", "'return'", "'='", "'.'", "'-'", "'!'", "'<'", "'>'", 
			"'<='", "'>='", "'=='", "'!='", "'*'", "'/'", "'%'", "'+'", "'&&'", "'||'", 
			"'''", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "ID", "NUM", "CHAR", "WS", "COMMENT", "LINE_COMMENT"
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
			setState(52);
			match(T__0);
			setState(53);
			match(T__1);
			setState(54);
			match(T__2);
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__14))) != 0)) {
				{
				{
				setState(55);
				declaration();
				}
				}
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(61);
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
			setState(66);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(63);
				structDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(64);
				varDeclaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(65);
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
			setState(79);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(68);
				varType();
				setState(69);
				match(ID);
				setState(70);
				match(T__4);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(72);
				varType();
				setState(73);
				match(ID);
				setState(74);
				match(T__5);
				setState(75);
				match(NUM);
				setState(76);
				match(T__6);
				setState(77);
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
			setState(81);
			match(T__7);
			setState(82);
			match(ID);
			setState(83);
			match(T__2);
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10))) != 0)) {
				{
				{
				setState(84);
				varDeclaration();
				}
				}
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(90);
			match(T__3);
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(91);
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
			setState(100);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(94);
				match(T__8);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(95);
				match(T__9);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(96);
				match(T__10);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(97);
				match(T__7);
				setState(98);
				match(ID);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(99);
				structDeclaration();
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
			setState(102);
			methodType();
			setState(103);
			match(ID);
			setState(104);
			match(T__11);
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__14))) != 0)) {
				{
				{
				setState(105);
				parameter();
				setState(110);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__12) {
					{
					{
					setState(106);
					match(T__12);
					setState(107);
					parameter();
					}
					}
					setState(112);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(118);
			match(T__13);
			setState(119);
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
			setState(121);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__14))) != 0)) ) {
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
			setState(132);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(123);
				parameterType();
				setState(124);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(126);
				parameterType();
				setState(127);
				match(ID);
				setState(128);
				match(T__5);
				setState(129);
				match(T__6);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(131);
				match(T__14);
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
			setState(134);
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
			setState(136);
			match(T__2);
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10))) != 0)) {
				{
				{
				setState(137);
				varDeclaration();
				}
				}
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__4) | (1L << T__11) | (1L << T__15) | (1L << T__17) | (1L << T__18) | (1L << T__21) | (1L << T__22) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << ID) | (1L << NUM))) != 0)) {
				{
				{
				setState(143);
				statement();
				}
				}
				setState(148);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(149);
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
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Stat_ifContext extends StatementContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public Stat_ifContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Stat_returnContext extends StatementContext {
		public ExpressionOomContext expressionOom() {
			return getRuleContext(ExpressionOomContext.class,0);
		}
		public Stat_returnContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Stat_assignmentContext extends StatementContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Stat_assignmentContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Stat_elseContext extends StatementContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public Stat_elseContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Stat_blockContext extends StatementContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public Stat_blockContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Stat_lineContext extends StatementContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Stat_lineContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class Stat_mcallContext extends StatementContext {
		public MethodCallContext methodCall() {
			return getRuleContext(MethodCallContext.class,0);
		}
		public Stat_mcallContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_statement);
		int _la;
		try {
			setState(182);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				_localctx = new Stat_ifContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(151);
				match(T__15);
				setState(152);
				match(T__11);
				setState(153);
				expression(0);
				setState(154);
				match(T__13);
				setState(155);
				block();
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__16) {
					{
					setState(156);
					match(T__16);
					setState(157);
					block();
					}
				}

				}
				break;
			case 2:
				_localctx = new Stat_elseContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(160);
				match(T__17);
				setState(161);
				match(T__11);
				setState(162);
				expression(0);
				setState(163);
				match(T__13);
				setState(164);
				block();
				}
				break;
			case 3:
				_localctx = new Stat_returnContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(166);
				match(T__18);
				setState(167);
				expressionOom();
				setState(168);
				match(T__4);
				}
				break;
			case 4:
				_localctx = new Stat_mcallContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(170);
				methodCall();
				setState(171);
				match(T__4);
				}
				break;
			case 5:
				_localctx = new Stat_blockContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(173);
				block();
				}
				break;
			case 6:
				_localctx = new Stat_assignmentContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(174);
				location();
				setState(175);
				match(T__19);
				setState(176);
				expression(0);
				}
				break;
			case 7:
				_localctx = new Stat_lineContext(_localctx);
				enterOuterAlt(_localctx, 7);
				{
				setState(179);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__21) | (1L << T__22) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << ID) | (1L << NUM))) != 0)) {
					{
					setState(178);
					expression(0);
					}
				}

				setState(181);
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
			setState(186);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__11:
			case T__21:
			case T__22:
			case T__35:
			case T__36:
			case T__37:
			case ID:
			case NUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(184);
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
			setState(194);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(188);
				match(ID);
				}
				break;
			case 2:
				{
				setState(189);
				match(ID);
				setState(190);
				match(T__5);
				setState(191);
				expression(0);
				setState(192);
				match(T__6);
				}
				break;
			}
			setState(198);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(196);
				match(T__20);
				setState(197);
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
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	 
		public ExpressionContext() { }
		public void copyFrom(ExpressionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class Expr_literalContext extends ExpressionContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public Expr_literalContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_locContext extends ExpressionContext {
		public LocationContext location() {
			return getRuleContext(LocationContext.class,0);
		}
		public Expr_locContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_parenthesisContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Expr_parenthesisContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_mcallContext extends ExpressionContext {
		public MethodCallContext methodCall() {
			return getRuleContext(MethodCallContext.class,0);
		}
		public Expr_mcallContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_minusContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Expr_minusContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_arith1Context extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_firstContext arith_op_first() {
			return getRuleContext(Arith_op_firstContext.class,0);
		}
		public Expr_arith1Context(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_arith2Context extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_secondContext arith_op_second() {
			return getRuleContext(Arith_op_secondContext.class,0);
		}
		public Expr_arith2Context(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_notContext extends ExpressionContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Expr_notContext(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_arith3Context extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_thirdContext arith_op_third() {
			return getRuleContext(Arith_op_thirdContext.class,0);
		}
		public Expr_arith3Context(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_arith4Context extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_fourthContext arith_op_fourth() {
			return getRuleContext(Arith_op_fourthContext.class,0);
		}
		public Expr_arith4Context(ExpressionContext ctx) { copyFrom(ctx); }
	}
	public static class Expr_arith5Context extends ExpressionContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public Arith_op_fifthContext arith_op_fifth() {
			return getRuleContext(Arith_op_fifthContext.class,0);
		}
		public Expr_arith5Context(ExpressionContext ctx) { copyFrom(ctx); }
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
			setState(212);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				_localctx = new Expr_mcallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(201);
				methodCall();
				}
				break;
			case 2:
				{
				_localctx = new Expr_locContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(202);
				location();
				}
				break;
			case 3:
				{
				_localctx = new Expr_literalContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(203);
				literal();
				}
				break;
			case 4:
				{
				_localctx = new Expr_minusContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(204);
				match(T__21);
				setState(205);
				expression(8);
				}
				break;
			case 5:
				{
				_localctx = new Expr_notContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(206);
				match(T__22);
				setState(207);
				expression(7);
				}
				break;
			case 6:
				{
				_localctx = new Expr_parenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(208);
				match(T__11);
				setState(209);
				expression(0);
				setState(210);
				match(T__13);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(236);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(234);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
					case 1:
						{
						_localctx = new Expr_arith5Context(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(214);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(215);
						arith_op_fifth();
						setState(216);
						expression(6);
						}
						break;
					case 2:
						{
						_localctx = new Expr_arith4Context(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(218);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(219);
						arith_op_fourth();
						setState(220);
						expression(5);
						}
						break;
					case 3:
						{
						_localctx = new Expr_arith3Context(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(222);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(223);
						arith_op_third();
						setState(224);
						expression(4);
						}
						break;
					case 4:
						{
						_localctx = new Expr_arith2Context(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(226);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(227);
						arith_op_second();
						setState(228);
						expression(3);
						}
						break;
					case 5:
						{
						_localctx = new Expr_arith1Context(new ExpressionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(230);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(231);
						arith_op_first();
						setState(232);
						expression(2);
						}
						break;
					}
					} 
				}
				setState(238);
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
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public MethodCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_methodCall; }
	}

	public final MethodCallContext methodCall() throws RecognitionException {
		MethodCallContext _localctx = new MethodCallContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_methodCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			match(ID);
			setState(240);
			match(T__11);
			setState(249);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__21) | (1L << T__22) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << ID) | (1L << NUM))) != 0)) {
				{
				setState(241);
				expression(0);
				setState(246);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__12) {
					{
					{
					setState(242);
					match(T__12);
					setState(243);
					expression(0);
					}
					}
					setState(248);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(251);
			match(T__13);
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
		enterRule(_localctx, 30, RULE_rel_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
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
		enterRule(_localctx, 32, RULE_eq_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(255);
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
		enterRule(_localctx, 34, RULE_arith_op_fifth);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__29) | (1L << T__30) | (1L << T__31))) != 0)) ) {
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
		enterRule(_localctx, 36, RULE_arith_op_fourth);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			_la = _input.LA(1);
			if ( !(_la==T__21 || _la==T__32) ) {
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
		enterRule(_localctx, 38, RULE_arith_op_third);
		try {
			setState(263);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__23:
			case T__24:
			case T__25:
			case T__26:
				enterOuterAlt(_localctx, 1);
				{
				setState(261);
				rel_op();
				}
				break;
			case T__27:
			case T__28:
				enterOuterAlt(_localctx, 2);
				{
				setState(262);
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
		enterRule(_localctx, 40, RULE_arith_op_second);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
			match(T__33);
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
		enterRule(_localctx, 42, RULE_arith_op_first);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(T__34);
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
		enterRule(_localctx, 44, RULE_literal);
		try {
			setState(272);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				int_literal();
				}
				break;
			case T__35:
				enterOuterAlt(_localctx, 2);
				{
				setState(270);
				char_literal();
				}
				break;
			case T__36:
			case T__37:
				enterOuterAlt(_localctx, 3);
				{
				setState(271);
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
		enterRule(_localctx, 46, RULE_int_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
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
		enterRule(_localctx, 48, RULE_char_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			match(T__35);
			setState(277);
			match(CHAR);
			setState(278);
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

	public static class Bool_literalContext extends ParserRuleContext {
		public Bool_literalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_literal; }
	}

	public final Bool_literalContext bool_literal() throws RecognitionException {
		Bool_literalContext _localctx = new Bool_literalContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_bool_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			_la = _input.LA(1);
			if ( !(_la==T__36 || _la==T__37) ) {
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3.\u011d\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\2\7\2;\n\2\f\2\16\2>\13\2\3\2\3\2\3"+
		"\3\3\3\3\3\5\3E\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4R\n"+
		"\4\3\5\3\5\3\5\3\5\7\5X\n\5\f\5\16\5[\13\5\3\5\3\5\5\5_\n\5\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\5\6g\n\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7o\n\7\f\7\16\7r\13"+
		"\7\7\7t\n\7\f\7\16\7w\13\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\5\t\u0087\n\t\3\n\3\n\3\13\3\13\7\13\u008d\n\13\f\13\16\13"+
		"\u0090\13\13\3\13\7\13\u0093\n\13\f\13\16\13\u0096\13\13\3\13\3\13\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00a1\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b6\n\f\3\f\5\f\u00b9"+
		"\n\f\3\r\3\r\5\r\u00bd\n\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00c5\n"+
		"\16\3\16\3\16\5\16\u00c9\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\5\17\u00d7\n\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17"+
		"\u00ed\n\17\f\17\16\17\u00f0\13\17\3\20\3\20\3\20\3\20\3\20\7\20\u00f7"+
		"\n\20\f\20\16\20\u00fa\13\20\5\20\u00fc\n\20\3\20\3\20\3\21\3\21\3\22"+
		"\3\22\3\23\3\23\3\24\3\24\3\25\3\25\5\25\u010a\n\25\3\26\3\26\3\27\3\27"+
		"\3\30\3\30\3\30\5\30\u0113\n\30\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33"+
		"\3\33\2\3\34\34\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62"+
		"\64\2\t\4\2\13\r\21\21\3\2\13\r\3\2\32\35\3\2\36\37\3\2 \"\4\2\30\30#"+
		"#\3\2\'(\2\u012c\2\66\3\2\2\2\4D\3\2\2\2\6Q\3\2\2\2\bS\3\2\2\2\nf\3\2"+
		"\2\2\fh\3\2\2\2\16{\3\2\2\2\20\u0086\3\2\2\2\22\u0088\3\2\2\2\24\u008a"+
		"\3\2\2\2\26\u00b8\3\2\2\2\30\u00bc\3\2\2\2\32\u00c4\3\2\2\2\34\u00d6\3"+
		"\2\2\2\36\u00f1\3\2\2\2 \u00ff\3\2\2\2\"\u0101\3\2\2\2$\u0103\3\2\2\2"+
		"&\u0105\3\2\2\2(\u0109\3\2\2\2*\u010b\3\2\2\2,\u010d\3\2\2\2.\u0112\3"+
		"\2\2\2\60\u0114\3\2\2\2\62\u0116\3\2\2\2\64\u011a\3\2\2\2\66\67\7\3\2"+
		"\2\678\7\4\2\28<\7\5\2\29;\5\4\3\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2"+
		"\2\2=?\3\2\2\2><\3\2\2\2?@\7\6\2\2@\3\3\2\2\2AE\5\b\5\2BE\5\6\4\2CE\5"+
		"\f\7\2DA\3\2\2\2DB\3\2\2\2DC\3\2\2\2E\5\3\2\2\2FG\5\n\6\2GH\7)\2\2HI\7"+
		"\7\2\2IR\3\2\2\2JK\5\n\6\2KL\7)\2\2LM\7\b\2\2MN\7*\2\2NO\7\t\2\2OP\7\7"+
		"\2\2PR\3\2\2\2QF\3\2\2\2QJ\3\2\2\2R\7\3\2\2\2ST\7\n\2\2TU\7)\2\2UY\7\5"+
		"\2\2VX\5\6\4\2WV\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3"+
		"\2\2\2\\^\7\6\2\2]_\7\7\2\2^]\3\2\2\2^_\3\2\2\2_\t\3\2\2\2`g\7\13\2\2"+
		"ag\7\f\2\2bg\7\r\2\2cd\7\n\2\2dg\7)\2\2eg\5\b\5\2f`\3\2\2\2fa\3\2\2\2"+
		"fb\3\2\2\2fc\3\2\2\2fe\3\2\2\2g\13\3\2\2\2hi\5\16\b\2ij\7)\2\2ju\7\16"+
		"\2\2kp\5\20\t\2lm\7\17\2\2mo\5\20\t\2nl\3\2\2\2or\3\2\2\2pn\3\2\2\2pq"+
		"\3\2\2\2qt\3\2\2\2rp\3\2\2\2sk\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3\2\2\2v"+
		"x\3\2\2\2wu\3\2\2\2xy\7\20\2\2yz\5\24\13\2z\r\3\2\2\2{|\t\2\2\2|\17\3"+
		"\2\2\2}~\5\22\n\2~\177\7)\2\2\177\u0087\3\2\2\2\u0080\u0081\5\22\n\2\u0081"+
		"\u0082\7)\2\2\u0082\u0083\7\b\2\2\u0083\u0084\7\t\2\2\u0084\u0087\3\2"+
		"\2\2\u0085\u0087\7\21\2\2\u0086}\3\2\2\2\u0086\u0080\3\2\2\2\u0086\u0085"+
		"\3\2\2\2\u0087\21\3\2\2\2\u0088\u0089\t\3\2\2\u0089\23\3\2\2\2\u008a\u008e"+
		"\7\5\2\2\u008b\u008d\5\6\4\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e"+
		"\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0094\3\2\2\2\u0090\u008e\3\2"+
		"\2\2\u0091\u0093\5\26\f\2\u0092\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094"+
		"\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3\2\2\2\u0096\u0094\3\2"+
		"\2\2\u0097\u0098\7\6\2\2\u0098\25\3\2\2\2\u0099\u009a\7\22\2\2\u009a\u009b"+
		"\7\16\2\2\u009b\u009c\5\34\17\2\u009c\u009d\7\20\2\2\u009d\u00a0\5\24"+
		"\13\2\u009e\u009f\7\23\2\2\u009f\u00a1\5\24\13\2\u00a0\u009e\3\2\2\2\u00a0"+
		"\u00a1\3\2\2\2\u00a1\u00b9\3\2\2\2\u00a2\u00a3\7\24\2\2\u00a3\u00a4\7"+
		"\16\2\2\u00a4\u00a5\5\34\17\2\u00a5\u00a6\7\20\2\2\u00a6\u00a7\5\24\13"+
		"\2\u00a7\u00b9\3\2\2\2\u00a8\u00a9\7\25\2\2\u00a9\u00aa\5\30\r\2\u00aa"+
		"\u00ab\7\7\2\2\u00ab\u00b9\3\2\2\2\u00ac\u00ad\5\36\20\2\u00ad\u00ae\7"+
		"\7\2\2\u00ae\u00b9\3\2\2\2\u00af\u00b9\5\24\13\2\u00b0\u00b1\5\32\16\2"+
		"\u00b1\u00b2\7\26\2\2\u00b2\u00b3\5\34\17\2\u00b3\u00b9\3\2\2\2\u00b4"+
		"\u00b6\5\34\17\2\u00b5\u00b4\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3"+
		"\2\2\2\u00b7\u00b9\7\7\2\2\u00b8\u0099\3\2\2\2\u00b8\u00a2\3\2\2\2\u00b8"+
		"\u00a8\3\2\2\2\u00b8\u00ac\3\2\2\2\u00b8\u00af\3\2\2\2\u00b8\u00b0\3\2"+
		"\2\2\u00b8\u00b5\3\2\2\2\u00b9\27\3\2\2\2\u00ba\u00bd\5\34\17\2\u00bb"+
		"\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\31\3\2\2"+
		"\2\u00be\u00c5\7)\2\2\u00bf\u00c0\7)\2\2\u00c0\u00c1\7\b\2\2\u00c1\u00c2"+
		"\5\34\17\2\u00c2\u00c3\7\t\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00be\3\2\2\2"+
		"\u00c4\u00bf\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c7\7\27\2\2\u00c7\u00c9"+
		"\5\32\16\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\33\3\2\2\2\u00ca"+
		"\u00cb\b\17\1\2\u00cb\u00d7\5\36\20\2\u00cc\u00d7\5\32\16\2\u00cd\u00d7"+
		"\5.\30\2\u00ce\u00cf\7\30\2\2\u00cf\u00d7\5\34\17\n\u00d0\u00d1\7\31\2"+
		"\2\u00d1\u00d7\5\34\17\t\u00d2\u00d3\7\16\2\2\u00d3\u00d4\5\34\17\2\u00d4"+
		"\u00d5\7\20\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00ca\3\2\2\2\u00d6\u00cc\3"+
		"\2\2\2\u00d6\u00cd\3\2\2\2\u00d6\u00ce\3\2\2\2\u00d6\u00d0\3\2\2\2\u00d6"+
		"\u00d2\3\2\2\2\u00d7\u00ee\3\2\2\2\u00d8\u00d9\f\7\2\2\u00d9\u00da\5$"+
		"\23\2\u00da\u00db\5\34\17\b\u00db\u00ed\3\2\2\2\u00dc\u00dd\f\6\2\2\u00dd"+
		"\u00de\5&\24\2\u00de\u00df\5\34\17\7\u00df\u00ed\3\2\2\2\u00e0\u00e1\f"+
		"\5\2\2\u00e1\u00e2\5(\25\2\u00e2\u00e3\5\34\17\6\u00e3\u00ed\3\2\2\2\u00e4"+
		"\u00e5\f\4\2\2\u00e5\u00e6\5*\26\2\u00e6\u00e7\5\34\17\5\u00e7\u00ed\3"+
		"\2\2\2\u00e8\u00e9\f\3\2\2\u00e9\u00ea\5,\27\2\u00ea\u00eb\5\34\17\4\u00eb"+
		"\u00ed\3\2\2\2\u00ec\u00d8\3\2\2\2\u00ec\u00dc\3\2\2\2\u00ec\u00e0\3\2"+
		"\2\2\u00ec\u00e4\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee"+
		"\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\35\3\2\2\2\u00f0\u00ee\3\2\2"+
		"\2\u00f1\u00f2\7)\2\2\u00f2\u00fb\7\16\2\2\u00f3\u00f8\5\34\17\2\u00f4"+
		"\u00f5\7\17\2\2\u00f5\u00f7\5\34\17\2\u00f6\u00f4\3\2\2\2\u00f7\u00fa"+
		"\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa"+
		"\u00f8\3\2\2\2\u00fb\u00f3\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3\2"+
		"\2\2\u00fd\u00fe\7\20\2\2\u00fe\37\3\2\2\2\u00ff\u0100\t\4\2\2\u0100!"+
		"\3\2\2\2\u0101\u0102\t\5\2\2\u0102#\3\2\2\2\u0103\u0104\t\6\2\2\u0104"+
		"%\3\2\2\2\u0105\u0106\t\7\2\2\u0106\'\3\2\2\2\u0107\u010a\5 \21\2\u0108"+
		"\u010a\5\"\22\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a)\3\2\2\2"+
		"\u010b\u010c\7$\2\2\u010c+\3\2\2\2\u010d\u010e\7%\2\2\u010e-\3\2\2\2\u010f"+
		"\u0113\5\60\31\2\u0110\u0113\5\62\32\2\u0111\u0113\5\64\33\2\u0112\u010f"+
		"\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0111\3\2\2\2\u0113/\3\2\2\2\u0114"+
		"\u0115\7*\2\2\u0115\61\3\2\2\2\u0116\u0117\7&\2\2\u0117\u0118\7+\2\2\u0118"+
		"\u0119\7&\2\2\u0119\63\3\2\2\2\u011a\u011b\t\b\2\2\u011b\65\3\2\2\2\32"+
		"<DQY^fpu\u0086\u008e\u0094\u00a0\u00b5\u00b8\u00bc\u00c4\u00c8\u00d6\u00ec"+
		"\u00ee\u00f8\u00fb\u0109\u0112";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}