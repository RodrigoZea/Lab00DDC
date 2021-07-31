# Lab00DDC
Laboratorio 0 de diseño de compiladores.

Herramienta utilizada:
ANTLR: https://www.antlr.org/

Gramática:
Decaf (se utilizó al especificación adjunta en Canvas)

Procedimiento (Java):
1. Correr el comando antlr Decaf.g4
2. Correr el comando javac Decaf*.java
3. Correr el comando grun Decaf program archivo.decaf -gui

En grun:
- Decaf hace referencia a la gramática
- Program a la primera instrucción 
- archivo.decaf se refiere al programa al cual generaremos su árbol sintáctico
- gui para desplegar el árbol sintáctico graficamente

--- 

Procedimiento (Python):
1. Correr el comando antlr -Dlanguage=Python3 Decaf.g4
2. Utilizar PyDecaf.py para aprovechar el parser y lexer generados por ANTLR.
3. Correr py PyDecaf.py archivo.decaf