import requests

url = "https://jsonplaceholder.typicode.com/users"
args = {"nombre": "Norman", "apellido": "Beltran"}
response = requests.get(url)

data = response.json()

print("_"*60)
for elemento in data:
    print(elemento["name"])
print("_"*60)

print(response)
print("Status code:", response.status_code)
print("URL:", response.url)
print("JSON:", response.json())