import requests


response = requests.get("http://localhost:7001/student/1")

print(response)
print("Status code:", response.status_code)
print("URL:", response.url)
print("JSON:", response.json())