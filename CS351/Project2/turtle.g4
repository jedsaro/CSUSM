grammar turtle;

start : expr | <EOF> ;

expr    
    : 'G01' whereto=NUMBER                 #drawLine    
    | 'G02' radius=NUMBER extent=NUMBER    #drawCircle
    | 'G28'                                #returnHome
    | 'G68'   clock=NUMBER                 #rotate
    | 'print' x_cord=NUMBER y_cord=NUMBER  #printValues 
    ;
NUMBER : ('0' .. '9') + ('.' ('0' .. '9') +)?;
WS : [ \r\n\t]+ -> skip;
