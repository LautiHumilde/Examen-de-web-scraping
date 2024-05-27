import requests
import json
import os

url = "https://jsonplaceholder.typicode.com/posts"
respuesta = requests.get(url)

if respuesta.status_code == 200:
  publicaciones = respuesta.json()
  
  datos_totales = []
  
  for lista in publicaciones:
    datos = {
      "id": lista["id"],
      "titulo": lista["title"],
      "contenido": lista["body"]
    }
  datos_totales.append(datos)
  
  with open("todas_las_publicaciones.json", "w") as archivo:
    json.dump(datos_totales, archivo, indent=4)
  
  print("Descarga completa en un solo archivo JSON.")
else:
  print(f"Error en la solicitud: {respuesta.status_code}")