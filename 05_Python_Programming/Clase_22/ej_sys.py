import sys

if len(sys.argv) > 1:
    for n in sys.argv[1:]:
        print(f"Hola {n}!")
else:
    print("Help ejecutar ej_sys con [n argumentos ]")        
    print("     Este script sirve para saludar a las personas ")        