import requests

url = "http://localhost:8880/form"

datos = { "name": "Juan Jose Paso",
          "email": "juanjose@paso.com",
          #"message": "",
          "message": "Por favor contactense conmigo por el producto publicado"
         }

r = requests.post(url, data=datos)

contenido = r.content.decode("utf-8")

if "Mensaje enviado" in contenido:
    print("Mensaje exitoso")
else:
    print("Error en el envio del mensaje")    

#print(contenido)