def upper_nombres(lista):
    for n in range(len(lista)):
        lista[n] = lista[n].upper()
    lista.append("FIN")
    

nombres = ["Ana", "Jose", "Juan"]

upper_nombres(nombres)
print(nombres)