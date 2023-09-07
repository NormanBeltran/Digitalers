
try:
    a = 10 + "A"
except ZeroDivisionError:
    print("Se intento dividir un numero por 0") 
except TypeError:
    print("Error de tipo de dato")      


print("Fin de Programa")
