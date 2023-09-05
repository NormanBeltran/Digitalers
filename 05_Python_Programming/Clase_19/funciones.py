# Funciones con argumentos opcionales
def potencia(base, exponente=2):
    return base**exponente

# Funciones con cantidad de argumentos indefinidos
def multiplicar(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

# Funciones con cantidad de keyword arguments indefinidos
def mostrar(**kwargs):

    for a,b in kwargs.items():
        print("clave", a, "valor", b)


a = 2
e = 3

#print(potencia(a, e))

#print(potencia(exponente=e, base=a))

#print(potencia(a))

#print(multiplicar(1,2,3,4,5,6,7))

mostrar(a=10, b=77, c=44)