f = open("peliculas.txt", "r")

#print(f.read())

c = 1
line = f.readline()
while line:
    print(f"linea {c}: {line}", end="")
    c += 1
    line = f.readline()


f.close()