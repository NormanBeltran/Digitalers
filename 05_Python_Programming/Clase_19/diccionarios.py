"""
Diccionarios

1. Mutables
2. Orden NO es importante
3. Las claves NO se pueden repetir elementos,
   Los valores SI se pueden repetir

"""

dic = {"Arg": 50, "Uru": 4, "Chi": 13, "Bra": 230}

dic["Par"] = 15
del dic["Chi"]
dic["Arg"] = 52

print(dic)