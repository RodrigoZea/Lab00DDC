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
WS : [ \t\r\n\f]+  ->channel(HIDDEN);

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
    : 'if' '(' expression ')' block ( 'else' block )?
    | 'while' '('expression')' block
    | 'return' expressionOom ';'
    | methodCall ';'
    | block
    | location '=' expression
    | (expression)? ';' 
    ;
expressionOom: expression |;
location: (ID|ID '[' expression ']') ('.' location)?;
expression 
    : location 
    | methodCall 
    | literal 
    | '-' expression // Unary Minus Operation
    | '!' expression // Unary NOT Operation
    | '('expression')'  
    | expression arith_op_fifth expression // * / % << >>
    | expression arith_op_fourth expression  // + -
    | expression arith_op_third expression // == != < <= > >=
    | expression arith_op_second expression // &&
    | expression arith_op_first expression // ||
    ;

methodCall: ID '(' arg1 ')';
// Puede ir algo que coincida con arg2 o nada, en caso de una llamada a metodo sin parametro
arg1: arg2 |;
// Expression y luego se utiliza * para permitir 0 o más parametros adicionales
arg2: (arg)(',' arg)*;
arg: expression; 

// Operaciones
// Divididas por nivel de precedencia
// Especificación de precedencia: https://anoopsarkar.github.io/compilers-class/decafspec.html
rel_op : '<' | '>' | '<=' | '>=' ;
eq_op : '==' | '!=' ;
arith_op_fifth: '*' | '/' | '%' | '<<' | '>>';
arith_op_fourth: '+' | '-';
arith_op_third: rel_op | eq_op;
arith_op_second: '&&';
arith_op_first: '||';

literal : int_literal | char_literal | bool_literal ;
int_literal : NUM ;
char_literal : '\'' CHAR '\'' ;
bool_literal : 'true' | 'false' ;