import time

#metodo tradicional
def suma_lineal(cant):
    suma = 0
    for numero in range(1,cant+1):
        suma += numero

    return suma


    # funcion lineal : 1 + n * 2 => 2n

#     queda:          O (n) lineal

metodo de gauss

def suma_continua(cant):
    return(cant/2) * (cant + 1)

# # 1 + 1 + 1 = 3 ==> O (1) constante

cantidad  = 100000
for i in range (4):
    t_0 = time.time()

suma1  =  suma_lineal ( cantidad )

    t_1  =  tiempo . tiempo ()

    suma2  =  suma_continua ( cantidad )

    t_2  =  tiempo . tiempo ()

    print ( f " { suma1 } , { t_1  -  t_0 } " )
    print ( f " { suma2 } , { t_2  -  t_1 } " )

    cantidad  * =  10

# a medida que vamos aumentando datos , los algortimos van actuando diferente segun el paradigma que tengan, y en la cantidad de software.
# tambien depende del hardware que tenemos.
