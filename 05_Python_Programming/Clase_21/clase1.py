# Clases y Objetos en Python
# Abstracción, Encapsulamiento


class Alumno:
    
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre  # Encapsulado
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"{self.apellido}, {self.__nombre}"

    def __eq__(self, obj):
        if  self.dni == obj.dni:
            return True
        return False

    def get_nombre(self):
        return self.__nombre


norman = Alumno("Norman", "Beltran", 123456)
pepe = Alumno("Lorenzo", "Beltran", 987654)

pepe.dni = 888888

print(norman.get_nombre(), norman.apellido, norman.dni)

print(norman, norman.dni)
print(pepe, pepe.dni)

if norman == pepe:
    print(f"Ambos objetos son iguales {norman}, {pepe}")
else:
    print(f"No son iguales {norman}, {pepe}")