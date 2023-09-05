lista = [1,2,3,4,5,6,7,8,10,1,2,3,4]

# Sumar todos los elementos a excepción del último

# Resolucion 1
resultado = sum(lista)-lista[-1]
print("resultado=", resultado)

# Resolucion 2
resultado = 0
for i in lista[:-1]:
    resultado += i

print("resultado=", resultado)

# Resolucion 3
resultado = sum(lista[:-1])
print("resultado=", resultado)