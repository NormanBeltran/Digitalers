# POST

import requests


lista = [{"name":"Pedro", "courses":10 },
               {"name":"Maria", "courses":11 },
               {"name":"Juan", "courses":9 },
               {"name":"Ana", "courses":12 },
               {"name":"Jose", "courses":1 },
               ]
for e in lista:
    response = requests.post("http://localhost:7001/student", json=e)

print(response)
print("Status code:", response.status_code)
print("URL:", response.url)
print("JSON:", response.json())