
# 5! = 5 * 4! = 120
# 4! = 4 * 3! = 24
# 3! = 3 * 2! = 6
# 2! = 2 * 1! = 2
# 1! = 1 * 0! = 1
# 0! = 1 = 1

#% * 4 * 3 * 2 * 1

def  factorial (numero):
    if  numero  ==  0 :
        return  1
    else:
        print ( f "soy el { numero } " )
        #recur = factorial(numero -1)
        #da = recur * numero
        #return da

# LOS PRINTS SON UTILIUZADOS EN ESTE CAS PARA MOSTRAR COMO ES LA RECURSIIDAD, CON UN PRINT ESTARIA BIEN. LA RECURSIVIDAD SE DA DE ARRIBA PARA ABAJO Y CUANDO HAY UN RETURN VUELVE DE ABAJO PARA ARRIBA.

# DESDE recur hasta return se puede achicar a solo una linea y va a hacer lo mismo, quedaria asi:

        return  factorial ( numero  - 1 ) *  numero

print(factorial(5))


# OTRO EJEMPLO MAS: EJEMPLO DE FIBONACCI, es una doble recursion basicamente.

    #fibonacci(0) = 1
    #fibonacci(1) = 1
    #fibonacci(n) = fibonacci(n-1)+fobonacci(n-2):

#TRADUCIDO EN PYTHON LUCE ASI:



def  sacarFibonacci ( numero ):
    if  numero  ==  0  or  numero  ==  1 :
        return  1
    else:
        return  sacarFibonacci ( numero  - 1 ) +  sacarFibonacci ( numero  -  2 )

print(sacarFibonacci ( 10 ))
