# Polimorfismo, Herencia

class Figura:
    tipo = "Figura geométrica"

    def __init__(self):
        self.ejemplo = "Ejemplo atributo de Figura"

    def area(self):
        pass
    def perimetro(self):
        pass
    def __str__(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (self.base*2)+(self.altura*2)
    
    def __str__(self):
        return f"Rectangulo de base {self.base} y altura {self.altura}"
    
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return (self.lado*4)
    
    def __str__(self):
        return f"Cuadrado de lado {self.lado}"    
    
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio**2
    
    def perimetro(self):
        return self.radio*2*3.14
    
    def __add__(self, obj):
        return self.radio + obj.radio
    
    def __len__(self):
        return int(self.perimetro())
    
    def __del__(self):
        print(f"Se esta borrando el circulo de radio {self.radio}")

    def __str__(self):
        return f"Circulo de radio {self.radio}"        
    
rec = Rectangulo(10, 5)    
cua = Cuadrado(20)

cir = Circulo(10)
cir2 = Circulo(1000)

print(rec, rec.area())
print(cua, cua.area())
print(cir, cir.area())

print("_"*60)
print(cir + cir2)
print(len(cir), cir.perimetro())

print("_"*60)
print(rec.tipo)
print(cua.tipo)
print(cir.tipo)

print(rec.ejemplo)