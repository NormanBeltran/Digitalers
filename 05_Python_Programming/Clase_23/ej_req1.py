"""
1xx Respuestas Informativas
2xx Peticiones correctas
3xx Redirecciones
4xx Errores del clientes
5xx Errores del servidor

"""

import requests

try:
    r = requests.get("https://www.infobae.com")
except Exception as e:
    print("Error:", e)    
else:    
    print(r.status_code)