# Waffle
Waffle is a new programming language with a language description and its own compiler. Created only for academic purposes.

## Grammar
decls 		→ decl, decls | Ɛ  
decl 		→ int ID | str ID | real ID  
functiondecl	→ fun ID ( decls ) compoundstat  
stat 		→ ifstat | loopstat | assgstat | compoundstat  
compoundstat → { stats }  
stats 		→ stat stats | Ɛ  
ifstat 		→ if ( boolexpr ) stat else stat | if ( boolexp ) stat  
loopstat	→ loop ( boolexpr ) stat  
assgnstat 	→ ID assgnop arithexpr ;  
assgnop	→ = | \*= | /= | %= | += | -=  
boolexp	→ aritexp boolop aritexp  
boolop		→ < | > | <= | >= | == | !=  
logexp		→ aritexp logop aritexp  
logop		→ and | or  
unaryexp	→ unaryop aritexp  
unaryop	→ + | - | ! | ++ | --  
aritexp 		→ aritexpr + multexp | aritexp - multexp | multexp  
multexp	→ multexpr*simpleexpr | multexp/simplexp | simplexp  
simplexp 	→ ID | INTNUM | REALNUM | STRING | ( aritexp )  

## Lexical Structure
**Comments:** Comments start with the # character and end with the end of line character.  
**Keywords:** int, str, real, fun, if, else, loop, and, or  
**Identifiers:** An identifier includes only lower case letters or underscores. A keyword cannot be an identifier.  
**Operators:** < | > | <= | >= | == | != | < | > | <= | >= | == | != | and | or  
**Delimiters:** whitespace, tab, newline  
**Numbers:** 
digit 		→ 0 | 1 | 2 | 3 | 4 | 5 | 6  | 7 | 8 | 9  
intnumber 	→ digit+  
fraction  	→ .digit+  
realnumber  	→ digit+ fraction ( exponent |  Ɛ)  

## Contributors

[Elif Balcı](https://www.elifbalci.com)  
[Can Berk Durmuş](https://www.canberkdurmus.com)  
[Ali Anıl Reyhan](https://www.anilreyhan.com)  