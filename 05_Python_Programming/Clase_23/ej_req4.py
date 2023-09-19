import requests

url = "https://www.infobae.com/economia/2023/09/18/creditos-anses-como-solicitar-hasta-40000-requisitos-y-limites-de-la-linea-que-entra-en-vigencia-hoy/"
response = requests.get(url)


print(response)
print("Status code:", response.status_code)
print("URL:", response.url)
print("Contenido:", response.content.decode("utf-8"))