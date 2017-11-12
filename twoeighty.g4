grammar twoeighty;

program         : variableDec* loop (statement ';')*;
variableDec     : ID '=' value ';';
loop            : INT unit=('ms'|'s') ':';
statement       : clear
                | colour
                | shape
                | increment
                | decrement
                | variableAssign;

clear           : 'clr' | 'clear';
colour          : ('colour' | '#') COLOUR;
shape           : rectangle | circle | line | arc ;
rectangle       : ('rect' | 'r') x=value ',' y=value ',' w=value ',' h=value;
circle          : ('circle' | 'c') x=value ',' y=value ',' r=value;
line            : ('line' | 'l') x1=value ',' y1=value ',' x2=value ',' y2=value;
arc             : ('arc' | 'a') x1=value ',' y1=value ',' x2=value ',' y2=value ',' cx=value ',' cy=value;
                
increment       : ID '++';
decrement       : ID '--';

variableAssign  : ID '=' value;

value           : l=value op r=value    #Binop
                | funccall '(' value (',' value)* ')' #MathFunc
                | '%'                   #Thousand
                | ID                    #Variable
                | INT                   #Integer;

op              : '/'
                | '//'
                | '*'
                | '+'
                | '-'
                | '%'
                ;

funccall        : 'sin'
                | 'cos'
                | 'tan'
                | 'pow'
                | 'rand'
                ;


ID              : [a-z];
INT             : ('-')? [0-9]+;
COLOUR          : [0-9a-z]+;