

#
#def multiple (numeros):
#     if numeros % 5 == 0:
#        return True
#numeros  = [ 2 , 5 , 10 , 23 , 50 , 33 ]
#resultado = list(filter (múltiple, numeros))

#print(resultado)

 #SI QUEREMOS SIMPLIFICAR EN UNA LINEA DE CODIGO PODEMOS UTILIZAR LAMBDA PARA LO QUE ES FUNCION Y FILTER PARA LO QUE ES FILTRAR. ENTONCES QUEDARIA ASI:

resultado2  =  list(filter(lambda numero : numero  %  5  ==  0 , numeros ))

print(resultado2)
