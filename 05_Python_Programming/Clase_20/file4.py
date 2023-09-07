
with open("peliculas.txt", "r") as f:
    c = 1
    line = f.readline()
    while line:
        print(f"linea {c}: {line}", end="")
        c += 1
        line = f.readline()

print("Fin de programa")