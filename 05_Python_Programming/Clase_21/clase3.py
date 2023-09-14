# Herencia Multiple

class Animals:

    def __init__(self, animals_name):
        print(animals_name, "es un animal")

    def sound(self):
        return "Animal Emite sonido"

class Mammal(Animals):

    def __init__(self, mammal_name):
        print(mammal_name, "es un mamifero")
        super().__init__(mammal_name)

class doNotFly(Mammal):
    def __init__(self, name):
        self.atributo1 = "AAA"
        print(name, "no puede volar")
        super().__init__(name)

class doNotSwim(Mammal):
    def __init__(self, name):
        self.atributo2 = "BBB"
        print(name, "no puede nadar")
        super().__init__(name)        

class Cat(doNotFly, doNotSwim):
    def __init__(self):
        print("Un gato")    
        super().__init__("Kitty") 
    
    def sound(self):
        return "Maullido"

gato = Cat()        
print("_"*60)
bat = doNotSwim("Murcielago")

print(gato.sound(), gato.atributo1, gato.atributo2)

print(Cat.__mro__)