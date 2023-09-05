"""
Listas

1. Mutables
2. Orden es importante
3. Se pueden repetir elementos

"""

nombres = [ "Sol", "Ailen", "Alfonsina", "Santiago", "Brisa", "Celeste" ]

# Mutabilidad: Agregar

nombres.append("Dahyana")
nombres.insert(2, "Norman")

print(nombres)

# Mutabilidad: Eliminar

nombres.pop()
del nombres[2]
print(nombres)

# Mutabilidad: Modificar

nombres[0] = "Sol Guadalupe"
print(nombres)


lista_ausentes = ["AB", "CN", "DD", "JP", "AB", "CN", "MM", "RP"]

print("Ausentes", lista_ausentes)