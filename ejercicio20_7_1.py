
def  merge_sort ( lista ):
    if  len ( lista ) <= 2 : # aca modificamos la condicion para que no nos de en decimales pero se llega a la conclusion que igual no se puede dividir entre 3 si la cantidad de elementos no nos permite porque igual quedara incompleto.
        print ("devuelve lista porque len <2")
        return lista
    medio  =  len ( lista ) // 3 # acá modificamos el 2 y ponemos 3 que es lo que pide el ejercicio
    print ("medio", medio) # aca modificamos el print para verlo
    izq  =  merge_sort ( lista [: medio ])
    print ("izq")
    medio2 = merge_sort(lista[medio: (medio * 2)])# aca agregamos el medio2 ya que ahora son tres mistades, darse cuenta que es un medio nuevo
    der  =  merge_sort ( lista [ (medio * 2):])# aca tambien mulltiplicamos medio * 2
    print (izq, medio2, der) # aca le agregamos medio2
    #return merge( izq , der, medio )# aca le agregamos medio

def  merge ( lista1 , lista2 ):
    i , j  =  0 , 0   # la i y la j lo utilizamos como
    resultado  = []

    while ( i  <  len ( lista1 ) and  j  <  len ( lista2 )):

        if ( lista1 [ i ] <  lista2 [ j ]):
            print ( f" lista 1 valor { lista1 [ i ] }   es menor a lista2   { lista2 [ j ] } " )
            resultado.append ( lista1 [ i ])
            i  +=  1
        else:
            print ( f" lista 2 valor { lista2 [ j ] }   es menor a lista1   { lista1 [ i ] } " )


            resultado.append ( lista2 [ j ])
            j  +=  1

    # Agregar lo que falta
    print ( "queda" , resultado )
    resultado  +=  lista1 [ i :]
    print ( "despues de agregar al resto I" , resultado )

    resultado  +=  lista2 [ j :]
    print ( "despues de agregar al resto J" , resultado )


    return  resultado


print ( merge_sort ([ 6 , 7 , - 1 , 0 , 5 , 2 , 3 , 8 ]))# aca si dividimos 8 numeros entre 3 no me van a quedar partes iguales pero me van a quedar una sublitsa izq, una sublista medio2 y una sublista der. pero cuando quiere dividir entre 3 nos dice el programa que la recursion llega hasta el infinito y quiere decir que quiere sacar la mitad un numero que no es divisible entre 3, entonces solo funciona bien cuando pones valores para dividir entre 3, entonces si ponemos 9 valores en vez de 8 nos funciona bien y nos da  los valores individuales, no siempre se va a tener listas que se dividan entre 3 claramente , entonces lo que podemos hacer es modificar la condicion que esta arriba if  len ( lista ) <  2 :, y queda <= 2, entonces cuando separa las sublistas aplicando la ultima condicion corregida nos divide en pares dos sublistas y queda una sublista incompleta, llegamos a la cnoclusion que no se puede dividir entre 3 si la cantidad de elementos no nos permite porque igual quedara incompleto.
