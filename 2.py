import random

def desordena(lista, cantidad_lista,contador):
    if contador < cantidad_lista:
        Numero_aleatorio =random.randint(contador,cantidad_lista-1)
        lista[contador],lista[Numero_aleatorio] = lista[Numero_aleatorio], lista[contador]
        desordena(lista,cantidad_lista,contador +1)
A=[1,2,3,4,5,6,7,8,9,10]
desordena(A, len(A),0)
print(A)    

#podemos notar que al ejecutar muchas veces el algoritmo que contiene una lista de 10 números,tenemos 
#en la salida diferentes números aleatorios  en cada ejecución.
