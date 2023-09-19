# Eliminar datos de un estudiante

import requests


response = requests.delete("http://localhost:7001/student/1")


print(response)
print("Status code:", response.status_code)
print("URL:", response.url)
#print("JSON:", response.json())