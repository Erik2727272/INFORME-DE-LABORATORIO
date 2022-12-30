#programa normal para calcular sucesión de fibonacci
"""import time
def fibonacci(n):
     a = 0
     b = 1
     for k in range(n+1):
         с = b+a
         a = b
         b = с
     return a
tiempo1=time.perf_counter()
fibonacci(5)
tiempo2=time.perf_counter()
print("Tiempo de ejecución de serie de fibonacci: ",tiempo2-tiempo1)"""

#Fibonacci no recursivo demoro:  2.9997900128364563e-06
# PS C:\Users\GigaByte\Documents\python> 

import time
def fibonacci_recursivo(numero):
     if numero == 0 or numero == 1:
         return 1
     else:
         return fibonacci_recursivo(numero-1)+fibonacci_recursivo(numero-2)
tiempo1=time.perf_counter()
fibonacci_recursivo(8)
tiempo2=time.perf_counter()
print ("Tiempo de ejecución de serie de fibonacci: :",tiempo2-tiempo1)


