// Generated from .\Decaf.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DecafParser}.
 */
public interface DecafListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DecafParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(DecafParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(DecafParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(DecafParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(DecafParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#varDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVarDeclaration(DecafParser.VarDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#varDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVarDeclaration(DecafParser.VarDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#structDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterStructDeclaration(DecafParser.StructDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#structDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitStructDeclaration(DecafParser.StructDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#varType}.
	 * @param ctx the parse tree
	 */
	void enterVarType(DecafParser.VarTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#varType}.
	 * @param ctx the parse tree
	 */
	void exitVarType(DecafParser.VarTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#methodDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterMethodDeclaration(DecafParser.MethodDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#methodDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitMethodDeclaration(DecafParser.MethodDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#methodType}.
	 * @param ctx the parse tree
	 */
	void enterMethodType(DecafParser.MethodTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#methodType}.
	 * @param ctx the parse tree
	 */
	void exitMethodType(DecafParser.MethodTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(DecafParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(DecafParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#parameterType}.
	 * @param ctx the parse tree
	 */
	void enterParameterType(DecafParser.ParameterTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#parameterType}.
	 * @param ctx the parse tree
	 */
	void exitParameterType(DecafParser.ParameterTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(DecafParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(DecafParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(DecafParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(DecafParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#expressionOom}.
	 * @param ctx the parse tree
	 */
	void enterExpressionOom(DecafParser.ExpressionOomContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#expressionOom}.
	 * @param ctx the parse tree
	 */
	void exitExpressionOom(DecafParser.ExpressionOomContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#location}.
	 * @param ctx the parse tree
	 */
	void enterLocation(DecafParser.LocationContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#location}.
	 * @param ctx the parse tree
	 */
	void exitLocation(DecafParser.LocationContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(DecafParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(DecafParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#methodCall}.
	 * @param ctx the parse tree
	 */
	void enterMethodCall(DecafParser.MethodCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#methodCall}.
	 * @param ctx the parse tree
	 */
	void exitMethodCall(DecafParser.MethodCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#arg1}.
	 * @param ctx the parse tree
	 */
	void enterArg1(DecafParser.Arg1Context ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#arg1}.
	 * @param ctx the parse tree
	 */
	void exitArg1(DecafParser.Arg1Context ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#arg2}.
	 * @param ctx the parse tree
	 */
	void enterArg2(DecafParser.Arg2Context ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#arg2}.
	 * @param ctx the parse tree
	 */
	void exitArg2(DecafParser.Arg2Context ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#arg}.
	 * @param ctx the parse tree
	 */
	void enterArg(DecafParser.ArgContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#arg}.
	 * @param ctx the parse tree
	 */
	void exitArg(DecafParser.ArgContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#rel_op}.
	 * @param ctx the parse tree
	 */
	void enterRel_op(DecafParser.Rel_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#rel_op}.
	 * @param ctx the parse tree
	 */
	void exitRel_op(DecafParser.Rel_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#eq_op}.
	 * @param ctx the parse tree
	 */
	void enterEq_op(DecafParser.Eq_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#eq_op}.
	 * @param ctx the parse tree
	 */
	void exitEq_op(DecafParser.Eq_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#arith_op_fifth}.
	 * @param ctx the parse tree
	 */
	void enterArith_op_fifth(DecafParser.Arith_op_fifthContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#arith_op_fifth}.
	 * @param ctx the parse tree
	 */
	void exitArith_op_fifth(DecafParser.Arith_op_fifthContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#arith_op_fourth}.
	 * @param ctx the parse tree
	 */
	void enterArith_op_fourth(DecafParser.Arith_op_fourthContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#arith_op_fourth}.
	 * @param ctx the parse tree
	 */
	void exitArith_op_fourth(DecafParser.Arith_op_fourthContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#arith_op_third}.
	 * @param ctx the parse tree
	 */
	void enterArith_op_third(DecafParser.Arith_op_thirdContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#arith_op_third}.
	 * @param ctx the parse tree
	 */
	void exitArith_op_third(DecafParser.Arith_op_thirdContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#arith_op_second}.
	 * @param ctx the parse tree
	 */
	void enterArith_op_second(DecafParser.Arith_op_secondContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#arith_op_second}.
	 * @param ctx the parse tree
	 */
	void exitArith_op_second(DecafParser.Arith_op_secondContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#arith_op_first}.
	 * @param ctx the parse tree
	 */
	void enterArith_op_first(DecafParser.Arith_op_firstContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#arith_op_first}.
	 * @param ctx the parse tree
	 */
	void exitArith_op_first(DecafParser.Arith_op_firstContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(DecafParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(DecafParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#int_literal}.
	 * @param ctx the parse tree
	 */
	void enterInt_literal(DecafParser.Int_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#int_literal}.
	 * @param ctx the parse tree
	 */
	void exitInt_literal(DecafParser.Int_literalContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#char_literal}.
	 * @param ctx the parse tree
	 */
	void enterChar_literal(DecafParser.Char_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#char_literal}.
	 * @param ctx the parse tree
	 */
	void exitChar_literal(DecafParser.Char_literalContext ctx);
	/**
	 * Enter a parse tree produced by {@link DecafParser#bool_literal}.
	 * @param ctx the parse tree
	 */
	void enterBool_literal(DecafParser.Bool_literalContext ctx);
	/**
	 * Exit a parse tree produced by {@link DecafParser#bool_literal}.
	 * @param ctx the parse tree
	 */
	void exitBool_literal(DecafParser.Bool_literalContext ctx);
}