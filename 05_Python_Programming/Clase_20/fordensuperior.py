# Funcion de orden superior, es aquella que recibe como argumento otra funcion

def cuadrado(x):
    return x**2

def cubo(x):
    return x**3

def mi_funcion(lista, funcion):
    resultado = []
    for n in lista:
        resultado.append(funcion(n))
    return resultado

enteros = [1,2,3,5,7]

print(mi_funcion(enteros, cubo))
