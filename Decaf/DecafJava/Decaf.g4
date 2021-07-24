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
structDeclaration:'struct' ID '{' (varDeclaration)* '}';
varType : 'int' | 'char' | 'boolean' | 'struct' ID | structDeclaration | 'void' ;
methodDeclaration: methodType ID '(' (parameter)* ')' block;
methodType: 'int'| 'char'| 'boolean' | 'void';
parameter
    : parameterType ID
    | parameterType ID '[' ']' 
    ;
parameterType: 'int' | 'char' | 'boolean';
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
    | expression op expression 
    | '-' expression 
    | '!' expression 
    | '('expression')'  
    ;
methodCall: ID '(' arg1 ')';
arg1: arg2 |;
arg2: (arg)(',' arg)*;
arg: expression; 
op: arith_op | rel_op | eq_op | cond_op  ;
arith_op : '+' | '-' | '*' | '/' | '%' ;
rel_op : '<' | '>' | '<=' | '>=' ;
eq_op : '==' | '!=' ;
cond_op : '&&' | '||' ;
literal : int_literal | char_literal | bool_literal ;
int_literal : NUM ;
char_literal : '\'' CHAR '\'' ;
bool_literal : 'true' | 'false' ;