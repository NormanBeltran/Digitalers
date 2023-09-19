# Modificar datos de un estudiante

import requests

datos = {"courses":999, "name":"Albert Einstein"}
response = requests.put("http://localhost:7001/student/1", json=datos)


print(response)
print("Status code:", response.status_code)
print("URL:", response.url)
#print("JSON:", response.json())