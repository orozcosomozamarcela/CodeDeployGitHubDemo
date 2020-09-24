
listaEntrada  = [ 3 , 2 , - 1 , 5 , 0 , 2 ]
#listaOrdenada  = [ - 1 , 3 , 4 , 5 , 6 , 7 ]

#En 2)
def  orden_insercion ( lista ):
    for  i  in  range ( len ( lista ) - 1 ): # N
        if  lista [ i + 1 ] <  lista [ i ]:
            reubicar ( lista , i + 1 )
        print ( "DEBUG:" , lista )

def  reubicar ( lista , pos ):
    valorPos  =  lista [ pos ]
    posOrig  =  pos
    print ( f "valor es { valorPos } para la posicion { posOrig } " )
    print ( f " { lista [ posOrig  -  1 ] } " )
    while  posOrig  >  0  y  valorPos  <  lista [ posOrig  -  1 ]: #N

        lista [ posOrig ] =  lista [ posOrig  -  1 ] # aca la secuencia que se ve en el ejercicio de insercion no hay problema de perder con los valores anteriores ya que es de menor a mayor.
        print ( f " { posOrig } es ahora { lista [ posOrig ] } " )
        posOrig  - =  1

    lista [ posOrig ] =  valorPos

orden_insercion ( listaEntrada )
