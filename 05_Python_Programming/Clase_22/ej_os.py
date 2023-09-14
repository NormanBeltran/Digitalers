import os

archivos = os.listdir("C:/temp")

for archivo in archivos:
    print(archivo)

print("Carpeta actual:", os.getcwd())    

#os.mkdir("NUEVA_CARPETA")
#os.rmdir("NUEVA_CARPETA")

#os.remove("C:/tmp/pepe.txt")
#os.rename("C:/tmp/pepe.txt", "C:/tmp/nuevo.txt")

#os.system("cls")
#os.system("notepad")

os.system("calc")