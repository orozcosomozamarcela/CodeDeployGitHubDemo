
listaEntrada  = [ 3 , 2 , - 1 , 5 , 0 , 2 ]

# por ejemplos si pedimos hasta acá que: print (lista[0])    # nos va a imprimir el valor 3 de la posición 0. Si yo pongo por ejemplo que me de el la posición -1 en vez de leer de izquierda a derecha me lee de derecha a izquierda entonces me va a dar el ultimo eemento de la lista, entonces me dara el valor 2. Y si le pido que me de por ejemplo la posicion 100 me va a dar error ya que esta fuera del rango de mi lista. Como haciamos para saber el valor de una posicion sin saber que posicion es???? Para eso utilizamos la posicion Leng que nos da la Longitud de ese elemento, de que elemento?? de la lista.

# En 2)
def  orden_seleccion ( lista ):
    ultimaPosicion  =  len ( lista ) -  1

    while  ultimaPosicion  >  0 : #N   # si o si tiene que haber mas de un elemento para ordenar
        mayorElemento  =  buscar_max ( lista , 0 , ultimaPosicion )
        lista [ mayorElemento ], lista [ ultimaPosicion ] =  lista [ ultimaPosicion ], lista [ mayorElemento ] # aca se esta haciendo una doble asignacion.
        print ( f "DEBUG: posicion mayor { mayorElemento } , ultima posicion { ultimaPosicion } , { lista } " )
        ultimaPosicion  =  ultimaPosicion  -  1


def  buscar_max ( lista , inicio , fin ):
    pos_max  =  inicio
    para  i  en  range ( inicio  + 1 , fin + 1 ): #N

        if  lista [ i ] >  lista [ pos_max ]:
            print ( f "posicion { i }  { lista [ i ] } es mayor que { pos_max }  { lista [ pos_max ] } " )
            pos_max  =  i
            print ( "pos_max es" , pos_max )

    return  pos_max

print ( listaEntrada )
orden_seleccion ( listaEntrada )
print ( listaEntrada )
