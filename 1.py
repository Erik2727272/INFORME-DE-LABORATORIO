import random

def desordena(lista, largo_lista,contador):
    if contador <largo_lista:
        Numero_random =random.randint(contador,largo_lista-1)
        lista[contador],lista[Numero_random] = lista[Numero_random], lista[contador]
        desordena(lista,largo_lista,contador +1)
A=[1,2,3,4,5,6,7,8,9]
desordena(A, len(A),0)
print(A)
