def seleccion_por_orden(lista, cantidad_lista, contador):
         if contador<cantidad_lista:
                 pequeño= lista[contador]
                 posicion= contador
                 for i in range(contador+1, cantidad_lista):
                          if lista[i]<pequeño:
                                  pequeño=lista[i]
                                  posicion=i
                 lista[contador],lista[posicion]=lista[posicion], lista[contador]
                 seleccion_por_orden (lista, cantidad_lista, contador+1)
A=[4, 3, 1, 9, 6, 10, 8, 7, 2, 5]
seleccion_por_orden((A), len(A),0)
print(A)
