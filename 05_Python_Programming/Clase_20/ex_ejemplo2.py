try:
    a = 10/0
except Exception as e:
    print("Ocurrio un error", e.__class__)     
else:
    print("Todo funciono bien sin excepciones")
finally:
    print("Fin de programa")    