from datetime import date

hoy = date.today()
micumple = date(2024,8,27)
faltan = abs(micumple-hoy)

print(f"Para mi proximo cumple faltan {faltan} dias")