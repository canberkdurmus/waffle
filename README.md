# Waffle

Waffle is a new programming language with a language description and its own compiler. Created only for academic
purposes. 

## Compiling Process Flow
- File should be read as array of lines  
- Lexical Analyzer cleans the comment lines, empty lines etc before starting the analysis (Preprocessor)  
- Every line that lexical analyzer read from the program file is tokenized as a LexLine  
- LexLines are appended as one dimensional array with $ symbols between the lines 
(This make us able to parse one line statements (assgnstat, returnstat etc) a lot easier in parsing phase)  
- Tokens from the lexical analyzer passed to the Parse Tree class initializer  
- Parser use the "get_next_token" to read the next token that that generated by Lexical Analyzer  
- Parser in the parse tree class executes a top-down recursive descent parsing operation  
- Parse Tree class also keeps the Symbol Table track while building the parse tree  
- Some parser checks (flow control) are completed while parse tree is being built 
(Because building a non balanced tree is actually traversing an unknown tree)  
- Some parser checks are being executed after the parse tree built (uniqueness, name-related)  
- Any error in the lexical analysis or parsing won't stop the compiling process, only error messages will be printed  


## Grammar

decls → decl, decls | Ɛ  
decl → int ID | str ID | real ID  
functiondecl → fun ID ( decls ) compoundstat  
stat → ifstat | loopstat | assgstat | compoundstat | returnstat | breakstat  
compoundstat → { stats }  
stats → stat stats | Ɛ  
ifstat → if ( boolexpr ) compundstat else compundstat | if ( boolexp ) compundstat  
loopstat → loop ( boolexpr ) compundstat  
assgnstat → ID assgnop arithexpr  
assgnop → =   
returnstat → return arithexp  
breakstat → break  
boolexp → aritexp boolop aritexp  
boolop → < | > | <= | >= | == | !=  
unaryexp → unaryop aritexp  
unaryop → + | -  
aritexp → aritexpr + multexp | aritexp - multexp | multexps  
multexp → multexpr*simpleexpr | multexp/simplexp | simplexp  
simplexp → ID | INTNUM | REALNUM | STRING | ( aritexp )

## Lexical Structure

**Comments:** Comments start with the # character and end with the end of line character.  
**Keywords:** int, str, real, fun, if, else, loop, and, or  
**Identifiers:** An identifier includes only lower case letters or underscores. A keyword cannot be an identifier.  
**Operators:** < | > | <= | >= | == | != | < | > | <= | >= | == | !=  
**Delimiters:** whitespace, tab, newline  
**Numbers:**
digit → 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  
intnumber → digit+  
fraction → .digit+  
realnumber → digit+ fraction ( exponent | Ɛ)
