import requests

url = "http://httpbin.org/get"
args = {"nombre": "Norman", "apellido": "Beltran"}
response = requests.get(url, params=args)

print(response)
print("Status code:", response.status_code)
print("URL:", response.url)
print("JSON:", response.json())