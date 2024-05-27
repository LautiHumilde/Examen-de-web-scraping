import requests
from key import API_KEY

def obtener_clima(ciudad):
  url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"
  respuesta = requests.get(url)
  if respuesta.status_code == 200:
    datos = respuesta.json()
    temperatura_actual = datos["main"]["temp"]
    sensacion_termica = datos["main"]["feels_like"]
    humedad = datos["main"]["humidity"]
    descripcion_clima = datos["weather"][0]["description"]
    return temperatura_actual, sensacion_termica, humedad, descripcion_clima
  else:
    try:
      error_mensaje = respuesta.json()["message"]
    except KeyError:
      error_mensaje = "error"
      print(f"No se pudo obtener la información: {respuesta.status_code} - {error_mensaje}")
      return None

def mostrar_informacion_clima(ciudad, temperatura_actual, sensacion_termica, humedad, descripcion_clima):
  informacion = (
    f"Información del clima para {ciudad}:\n"
    f"Temperatura: {temperatura_actual}°C\n"
    f"Sensación térmica: {sensacion_termica}°C\n"
    f"Humedad: {humedad}%\n"
    f"Descripción del clima: {descripcion_clima.capitalize()}"
)
  return informacion

def main():
  ciudad = input("Ingrese el nombre de la ciudad: ")
  datos_clima = obtener_clima(ciudad)
  if datos_clima:
    informacion_clima = mostrar_informacion_clima(ciudad, *datos_clima)
    print(informacion_clima)

main()
