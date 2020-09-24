
##Ejercicio 19.4.1. Implementar una función que recibe una lista y devuelva otra lista con los mismos elementos
#que la primera, ordenados de mayor a menor mediante el método de inserción.
# "" "

listaEntrada  = [ 3 , 2 , - 1 , 5 , 0 , 2 ]

#En 2)
def  orden_insercion ( lista ):
    listaNueva  =  lista.copy()  # aca ya no es necesario hacer un if porque no hay que hacer comparacion sino que ordenar de mayor a menor.
    for  i  in  range ( len ( listaNueva ) - 1 ): # N
        if  listaNueva [ i + 1 ] >  listaNueva [ i ]:
            reubicar ( listaNueva , i + 1 )
        print ( "DEBUG:" , listaNueva )
    return  listaNueva

def  reubicar ( listaNueva , pos ):
    valorPos  =  listaNueva [ pos ]
    posOrig  =  pos
    print ( f" valor es { valorPos } para la posicion { posOrig } " )
    print ( f" { listaNueva [ posOrig  -  1 ] } " )
    while  posOrig  >  0  and  valorPos  >  listaNueva [ posOrig  -  1 ]: #N
        listaNueva [ posOrig ] =  listaNueva [ posOrig - 1 ]
        listaNueva [ posOrig - 1 ] =  valorPos # tiene que ir seguido esta secuencia con la anterior porque sino evalua erroneamente el valor actual. y porque aca se ordena de mayor a menor.
        print ( f" { posOrig } es ahora { listaNueva [ posOrig ] } " )
        posOrig  -=  1

print ( orden_insercion ( listaEntrada ))
