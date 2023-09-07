def cuadrado(x):
    return x**2

def cubo(x):
    return x**3

enteros = [1,2,3,5,7]

print(tuple(map(cuadrado, enteros)))