import json
import requests

# URL del esquema OpenAPI (asegúrate de que el servidor esté corriendo)
url = "http://localhost:8000/openapi.json"
response = requests.get(url)

if response.status_code == 200:
    with open("postman_collection.json", "w") as f:
        json.dump(response.json(), f, indent=4)
    print("✅ Colección de Postman generada correctamente como 'postman_collection.json'.")
else:
    print(f"❌ Error al obtener OpenAPI: {response.status_code}")
