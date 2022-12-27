#programa normal para calcular factorial
"""import time
def factorial(n):
    b=1
    for i in range (n,1,-1):
        b=b*1
    return b
tiempo1=time.perf_counter()
A=factorial(5)
tiempo2=time.perf_counter()
print(A," .......tiempo de ejecución: ",tiempo2-tiempo1)"""

#1  .......tiempo de ejecución:  3.00002284348011e-06
# PS C:\Users\GigaByte\Documents\python> 


#programa recursivo para calcular factorial

import time
def factorial_recursivo(n):
     if n == 1:
         return 1
     return n*factorial_recursivo(n-1)
tiempo1=time.perf_counter()                  
B=factorial_recursivo(5)
tiempo2=time.perf_counter()
print(B," ......tiempo de ejecución: ",tiempo2-tiempo1)
