#Implemente un programa recursivo que calcule la potencia de un nu mero elevado a otro.
# Sabemos que 2n = 2n/2. 2n/2 donde n es un nro par; y 2n = 2(n-1)/2. 2(n-1)/2.2 si n es
# impar

def potencia(a,b):
    if b==1:
        return a
    else:
        return potencia(a,b-1)*a
