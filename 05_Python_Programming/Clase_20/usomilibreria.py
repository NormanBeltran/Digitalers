""" Uso de Librerias:1
import milibreria


print(milibreria.cuadrado(7))

for n in milibreria.provincias:
    print("La provincia mas linda es:", n)
"""

""" Uso de Librerias:2
import milibreria as ml

print(ml.cuadrado(7))

for n in ml.provincias:
    print("La provincia mas linda es:", n)
"""

from libreria.milibreria import cuadrado, provincias

print(cuadrado(7))

for n in provincias:
    print("La provincia mas linda es:", n)