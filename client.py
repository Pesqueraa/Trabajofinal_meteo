import requests
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def obtener_prediccion_meteorologica(ciudad, api_key):
    base_url = "http://api.weatherstack.com/current"
    parametros = {
        'access_key': api_key,
        'query': ciudad
    }

    respuesta = requests.get(base_url, params=parametros)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        temperatura = datos['current']['temperature']
        descripcion_clima = datos['current']['weather_descriptions'][0]
        velocidad_viento = datos['current']['wind_speed']

        prediccion = f"Pronóstico meteorológico para {ciudad}:\n"
        prediccion += f"Temperatura: {temperatura}°C\n"
        prediccion += f"Descripción del clima: {descripcion_clima}\n"
        prediccion += f"Velocidad del viento: {velocidad_viento} km/h\n"

        return prediccion
    else:
        return f"No se pudo obtener la información. Código de estado: {respuesta.status_code}"

def obtener_datos_ciudades_desde_archivo(archivo):
    try:
        datos = pd.read_csv(archivo)
        return datos['Ciudad'].tolist()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

def main():
    # Sustituir 'TU_API_KEY' por la clave de API de WeatherStack
    api_key = 'c3869c395e9ce787effb71f812b24247'
    
    # Cargar las ciudades desde un archivo de entrada
    archivo_ciudades = 'ciudades.csv'
    ciudades = obtener_datos_ciudades_desde_archivo(archivo_ciudades)

    if not ciudades:
        print("No se encontraron ciudades en el archivo.")
        return

    # Interfaz gráfica con PySimpleGUI
    layout = [[sg.Text('Selecciona una ciudad:')],
              [sg.Listbox(values=ciudades, size=(30, 10), key='ciudades')],
              [sg.Button('Mostrar Pronóstico'), sg.Button('Salir')]]

    window = sg.Window('Mapa del Tiempo', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Salir':
            break
        elif event == 'Mostrar Pronóstico':
            ciudad_seleccionada = values['ciudades'][0]
            pronostico = obtener_prediccion_meteorologica(ciudad_seleccionada, api_key)
            sg.popup(pronostico)

    window.close()

if __name__ == "__main__":
    main()
