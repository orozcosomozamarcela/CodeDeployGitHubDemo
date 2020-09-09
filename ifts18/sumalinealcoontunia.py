import time

metodo tradicional
def suma_lineal():
    suma = 0
    for numero in range(1,cant+1):
        suma += numero

    return suma

metodo de gauss

def suma_continua(cant):
    return(cant/2) * (cant + 1)


cantidad  = 100000
for i in range (4):
    t_0 = time.time()

print (suma_lineal(1000))
print (suma_continua(1000))

# a medida que vamos aumentando datos , los algortimos van actuando diferente segun el paradigma que tengan, y en la cantidad de software.
# tambien depende del hardware que tenemos.
