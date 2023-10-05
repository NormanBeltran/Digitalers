from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_sonido(self):
        pass

    @abstractmethod
    def caminar(self):
        pass

class Perro(Animal):
    def __init__(self):
        self.ladrar = "Guau"
    
    def emitir_sonido(self):
        return f"Ladra {self.ladrar}"
    

    
k = Perro()

print(k.emitir_sonido())
