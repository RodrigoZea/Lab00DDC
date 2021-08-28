// Define decaf grammar
grammar Decaf;

// Reglas LEXER
// Definiciones base para letras y digitos
fragment LETTER: ('a'..'z'|'A'..'Z'|'_');
fragment DIGIT: '0'..'9';
// Las otras reglas de lexer de Decaf 
ID: LETTER (LETTER|DIGIT)*;
NUM: DIGIT(DIGIT)*;
CHAR: '\'' ( ~['\r\n\\] | '\\' ['\\] ) '\'';
WS : [ \t\r\n\f]+  -> channel(HIDDEN);

COMMENT
    : '/*' .*? '*/' -> channel(2)
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> channel(2)
    ;

// -----------------------------------------------------------------------------------------------------------------------------------------

// Reglas PARSER
program:'class' 'Program' '{' (declaration)* '}';
declaration
    : structDeclaration
    | varDeclaration
    | methodDeclaration
    ;
varDeclaration
    : varType ID ';' 
    | varType ID '[' NUM ']' ';' 
    ;
structDeclaration:'struct' ID '{' (varDeclaration)* '}' (';')?;
varType 
    : 'int' 
    | 'char' 
    | 'boolean' 
    | 'struct' ID 
    | structDeclaration 
    | 'void' 
    ;
methodDeclaration: methodType ID '(' (parameter (',' parameter)*)* ')' block;
methodType
    : 'int'
    | 'char'
    | 'boolean' 
    | 'void'
    ;
parameter
    : parameterType ID
    | parameterType ID '[' ']' 
    | 'void'
    ;
parameterType
    : 'int' 
    | 'char' 
    | 'boolean'
    ;
block: '{' (varDeclaration)* (statement)* '}';
statement
    : 'if' '(' expression ')' block ( 'else' block )? #stat_if
    | 'while' '('expression')' block #stat_else
    | 'return' expressionOom ';' #stat_return
    | methodCall ';' #stat_mcall
    | block #stat_block
    | location '=' expression #stat_assignment
    | (expression)? ';' #stat_line
    ;
expressionOom: expression |;
location: (ID|ID '[' expression ']') ('.' location)?;
expression 
    : methodCall #expr_mcall
    | location #expr_loc
    | literal #expr_literal
    | '-' expression #expr_minus // Unary Minus Operation
    | '!' expression #expr_not // Unary NOT Operation
    | '('expression')' #expr_parenthesis
    | expression arith_op_fifth expression #expr_arith5 // * / %
    | expression arith_op_fourth expression #expr_arith4 // + -
    | expression arith_op_third expression #expr_arith3 // == != < <= > >=
    | expression arith_op_second expression #expr_arith2 // &&
    | expression arith_op_first expression #expr_arith1 // ||
    ;

methodCall: ID '(' (expression (',' expression)?)* ')';

// Operaciones
// Divididas por nivel de precedencia
// Especificación de precedencia: https://anoopsarkar.github.io/compilers-class/decafspec.html
rel_op : '<' | '>' | '<=' | '>=';
eq_op : '==' | '!=' ;
arith_op_fifth: '*' | '/' | '%';
arith_op_fourth: '+' | '-';
arith_op_third: rel_op | eq_op;
arith_op_second: '&&';
arith_op_first: '||';

// <arith_op>→'+'| '-'| '*'| '/'| '%'
// <rel_op>→'<'| '>'| '<='| '>='
// <eq_op>→'=='| '!='
// <cond_op>→'&&'| '||'

literal : int_literal | char_literal | bool_literal ;
int_literal : NUM ;
char_literal : '\'' CHAR '\'' ;
bool_literal : 'true' | 'false' ;