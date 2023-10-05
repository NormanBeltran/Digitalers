from collections import abc

class MiSet(abc.Set):
    def __init__(self, iterable):
        self.elements = []
        for value in iterable:
            if value not in self.elements:
                self.elements.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

    def __str__(self):
        return "".join(str(i) for i in self.elements)
    
s1 = MiSet("abcdefg")    
s2 = MiSet("efghij")    

print(s1 & s2)
print(s1 | s2)

for letra in s1:
    print(letra)

if "a" in s1:
    print("La letra a esta en s1")

print(len(s1))    