# Generated from Decaf.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete listener for a parse tree produced by DecafParser.
class DecafListener(ParseTreeListener):

    # Enter a parse tree produced by DecafParser#program.
    def enterProgram(self, ctx:DecafParser.ProgramContext):
        pass

    # Exit a parse tree produced by DecafParser#program.
    def exitProgram(self, ctx:DecafParser.ProgramContext):
        pass


    # Enter a parse tree produced by DecafParser#declaration.
    def enterDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#declaration.
    def exitDeclaration(self, ctx:DecafParser.DeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#varDeclaration.
    def enterVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#varDeclaration.
    def exitVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#structDeclaration.
    def enterStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#structDeclaration.
    def exitStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#varType.
    def enterVarType(self, ctx:DecafParser.VarTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#varType.
    def exitVarType(self, ctx:DecafParser.VarTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by DecafParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by DecafParser#methodType.
    def enterMethodType(self, ctx:DecafParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#methodType.
    def exitMethodType(self, ctx:DecafParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#parameter.
    def enterParameter(self, ctx:DecafParser.ParameterContext):
        pass

    # Exit a parse tree produced by DecafParser#parameter.
    def exitParameter(self, ctx:DecafParser.ParameterContext):
        pass


    # Enter a parse tree produced by DecafParser#parameterType.
    def enterParameterType(self, ctx:DecafParser.ParameterTypeContext):
        pass

    # Exit a parse tree produced by DecafParser#parameterType.
    def exitParameterType(self, ctx:DecafParser.ParameterTypeContext):
        pass


    # Enter a parse tree produced by DecafParser#block.
    def enterBlock(self, ctx:DecafParser.BlockContext):
        pass

    # Exit a parse tree produced by DecafParser#block.
    def exitBlock(self, ctx:DecafParser.BlockContext):
        pass


    # Enter a parse tree produced by DecafParser#stat_if.
    def enterStat_if(self, ctx:DecafParser.Stat_ifContext):
        pass

    # Exit a parse tree produced by DecafParser#stat_if.
    def exitStat_if(self, ctx:DecafParser.Stat_ifContext):
        pass


    # Enter a parse tree produced by DecafParser#stat_else.
    def enterStat_else(self, ctx:DecafParser.Stat_elseContext):
        pass

    # Exit a parse tree produced by DecafParser#stat_else.
    def exitStat_else(self, ctx:DecafParser.Stat_elseContext):
        pass


    # Enter a parse tree produced by DecafParser#stat_return.
    def enterStat_return(self, ctx:DecafParser.Stat_returnContext):
        pass

    # Exit a parse tree produced by DecafParser#stat_return.
    def exitStat_return(self, ctx:DecafParser.Stat_returnContext):
        pass


    # Enter a parse tree produced by DecafParser#stat_mcall.
    def enterStat_mcall(self, ctx:DecafParser.Stat_mcallContext):
        pass

    # Exit a parse tree produced by DecafParser#stat_mcall.
    def exitStat_mcall(self, ctx:DecafParser.Stat_mcallContext):
        pass


    # Enter a parse tree produced by DecafParser#stat_block.
    def enterStat_block(self, ctx:DecafParser.Stat_blockContext):
        pass

    # Exit a parse tree produced by DecafParser#stat_block.
    def exitStat_block(self, ctx:DecafParser.Stat_blockContext):
        pass


    # Enter a parse tree produced by DecafParser#stat_assignment.
    def enterStat_assignment(self, ctx:DecafParser.Stat_assignmentContext):
        pass

    # Exit a parse tree produced by DecafParser#stat_assignment.
    def exitStat_assignment(self, ctx:DecafParser.Stat_assignmentContext):
        pass


    # Enter a parse tree produced by DecafParser#stat_line.
    def enterStat_line(self, ctx:DecafParser.Stat_lineContext):
        pass

    # Exit a parse tree produced by DecafParser#stat_line.
    def exitStat_line(self, ctx:DecafParser.Stat_lineContext):
        pass


    # Enter a parse tree produced by DecafParser#expressionOom.
    def enterExpressionOom(self, ctx:DecafParser.ExpressionOomContext):
        pass

    # Exit a parse tree produced by DecafParser#expressionOom.
    def exitExpressionOom(self, ctx:DecafParser.ExpressionOomContext):
        pass


    # Enter a parse tree produced by DecafParser#location.
    def enterLocation(self, ctx:DecafParser.LocationContext):
        pass

    # Exit a parse tree produced by DecafParser#location.
    def exitLocation(self, ctx:DecafParser.LocationContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_literal.
    def enterExpr_literal(self, ctx:DecafParser.Expr_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_literal.
    def exitExpr_literal(self, ctx:DecafParser.Expr_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_loc.
    def enterExpr_loc(self, ctx:DecafParser.Expr_locContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_loc.
    def exitExpr_loc(self, ctx:DecafParser.Expr_locContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_parenthesis.
    def enterExpr_parenthesis(self, ctx:DecafParser.Expr_parenthesisContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_parenthesis.
    def exitExpr_parenthesis(self, ctx:DecafParser.Expr_parenthesisContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_mcall.
    def enterExpr_mcall(self, ctx:DecafParser.Expr_mcallContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_mcall.
    def exitExpr_mcall(self, ctx:DecafParser.Expr_mcallContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_minus.
    def enterExpr_minus(self, ctx:DecafParser.Expr_minusContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_minus.
    def exitExpr_minus(self, ctx:DecafParser.Expr_minusContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_arith1.
    def enterExpr_arith1(self, ctx:DecafParser.Expr_arith1Context):
        pass

    # Exit a parse tree produced by DecafParser#expr_arith1.
    def exitExpr_arith1(self, ctx:DecafParser.Expr_arith1Context):
        pass


    # Enter a parse tree produced by DecafParser#expr_arith2.
    def enterExpr_arith2(self, ctx:DecafParser.Expr_arith2Context):
        pass

    # Exit a parse tree produced by DecafParser#expr_arith2.
    def exitExpr_arith2(self, ctx:DecafParser.Expr_arith2Context):
        pass


    # Enter a parse tree produced by DecafParser#expr_not.
    def enterExpr_not(self, ctx:DecafParser.Expr_notContext):
        pass

    # Exit a parse tree produced by DecafParser#expr_not.
    def exitExpr_not(self, ctx:DecafParser.Expr_notContext):
        pass


    # Enter a parse tree produced by DecafParser#expr_arith3.
    def enterExpr_arith3(self, ctx:DecafParser.Expr_arith3Context):
        pass

    # Exit a parse tree produced by DecafParser#expr_arith3.
    def exitExpr_arith3(self, ctx:DecafParser.Expr_arith3Context):
        pass


    # Enter a parse tree produced by DecafParser#expr_arith4.
    def enterExpr_arith4(self, ctx:DecafParser.Expr_arith4Context):
        pass

    # Exit a parse tree produced by DecafParser#expr_arith4.
    def exitExpr_arith4(self, ctx:DecafParser.Expr_arith4Context):
        pass


    # Enter a parse tree produced by DecafParser#expr_arith5.
    def enterExpr_arith5(self, ctx:DecafParser.Expr_arith5Context):
        pass

    # Exit a parse tree produced by DecafParser#expr_arith5.
    def exitExpr_arith5(self, ctx:DecafParser.Expr_arith5Context):
        pass


    # Enter a parse tree produced by DecafParser#methodCall.
    def enterMethodCall(self, ctx:DecafParser.MethodCallContext):
        pass

    # Exit a parse tree produced by DecafParser#methodCall.
    def exitMethodCall(self, ctx:DecafParser.MethodCallContext):
        pass


    # Enter a parse tree produced by DecafParser#arg1.
    def enterArg1(self, ctx:DecafParser.Arg1Context):
        pass

    # Exit a parse tree produced by DecafParser#arg1.
    def exitArg1(self, ctx:DecafParser.Arg1Context):
        pass


    # Enter a parse tree produced by DecafParser#arg2.
    def enterArg2(self, ctx:DecafParser.Arg2Context):
        pass

    # Exit a parse tree produced by DecafParser#arg2.
    def exitArg2(self, ctx:DecafParser.Arg2Context):
        pass


    # Enter a parse tree produced by DecafParser#arg.
    def enterArg(self, ctx:DecafParser.ArgContext):
        pass

    # Exit a parse tree produced by DecafParser#arg.
    def exitArg(self, ctx:DecafParser.ArgContext):
        pass


    # Enter a parse tree produced by DecafParser#rel_op.
    def enterRel_op(self, ctx:DecafParser.Rel_opContext):
        pass

    # Exit a parse tree produced by DecafParser#rel_op.
    def exitRel_op(self, ctx:DecafParser.Rel_opContext):
        pass


    # Enter a parse tree produced by DecafParser#eq_op.
    def enterEq_op(self, ctx:DecafParser.Eq_opContext):
        pass

    # Exit a parse tree produced by DecafParser#eq_op.
    def exitEq_op(self, ctx:DecafParser.Eq_opContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_op_fifth.
    def enterArith_op_fifth(self, ctx:DecafParser.Arith_op_fifthContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_op_fifth.
    def exitArith_op_fifth(self, ctx:DecafParser.Arith_op_fifthContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_op_fourth.
    def enterArith_op_fourth(self, ctx:DecafParser.Arith_op_fourthContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_op_fourth.
    def exitArith_op_fourth(self, ctx:DecafParser.Arith_op_fourthContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_op_third.
    def enterArith_op_third(self, ctx:DecafParser.Arith_op_thirdContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_op_third.
    def exitArith_op_third(self, ctx:DecafParser.Arith_op_thirdContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_op_second.
    def enterArith_op_second(self, ctx:DecafParser.Arith_op_secondContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_op_second.
    def exitArith_op_second(self, ctx:DecafParser.Arith_op_secondContext):
        pass


    # Enter a parse tree produced by DecafParser#arith_op_first.
    def enterArith_op_first(self, ctx:DecafParser.Arith_op_firstContext):
        pass

    # Exit a parse tree produced by DecafParser#arith_op_first.
    def exitArith_op_first(self, ctx:DecafParser.Arith_op_firstContext):
        pass


    # Enter a parse tree produced by DecafParser#literal.
    def enterLiteral(self, ctx:DecafParser.LiteralContext):
        pass

    # Exit a parse tree produced by DecafParser#literal.
    def exitLiteral(self, ctx:DecafParser.LiteralContext):
        pass


    # Enter a parse tree produced by DecafParser#int_literal.
    def enterInt_literal(self, ctx:DecafParser.Int_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#int_literal.
    def exitInt_literal(self, ctx:DecafParser.Int_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#char_literal.
    def enterChar_literal(self, ctx:DecafParser.Char_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#char_literal.
    def exitChar_literal(self, ctx:DecafParser.Char_literalContext):
        pass


    # Enter a parse tree produced by DecafParser#bool_literal.
    def enterBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by DecafParser#bool_literal.
    def exitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        pass



del DecafParser