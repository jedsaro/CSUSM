grammar turtle;

start : expr | <EOF> ;

expr    

    : 'G01'   x_cord=NUMBER  y_cord=NUMBER    #drawLine    
    | 'G02'   radius=NUMBER extent=NUMBER     #drawCircle
    | 'M05'                                   #removepen
    | 'M03'                                   #addpen
    | 'G68'   clock=NUMBER                    #rotate
    ;

NUMBER : ('-')? ('0' .. '9') + ('.' ('0' .. '9') +)?;
WS : [ \r\n\t]+ -> skip;
