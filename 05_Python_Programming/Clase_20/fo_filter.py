def bisiesto(anio):
    if (anio%400==0) or (anio%4==0 and anio%100!=0):
        return True
    return False

anios = [1840, 2000, 1992, 1993, 1998, 1987, 1986]

print(list(filter(bisiesto, anios)))