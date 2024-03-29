import numpy as np
import requests
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

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

        prediccion = f"{ciudad}:\n"
        prediccion += f"Temperatura: {temperatura}°C\n"
        prediccion += f"Descripción del clima: {descripcion_clima}\n"
        prediccion += f"Velocidad del viento: {velocidad_viento} km/h\n"

        return prediccion
    else:
        return f"No se pudo obtener la información. Código de estado: {respuesta.status_code}"

def obtener_datos_ciudades_desde_archivo(archivo):
    try:
        datos = pd.read_csv(archivo)
        return datos[['Ciudad', 'Latitud', 'Longitud']]
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return pd.DataFrame()

def dibujar_mapa(datos, api_key):
    sg.theme('LightGrey1')

    ciudades = datos['Ciudad'].tolist()

    layout = [[sg.Text('Selecciona una ciudad:')],
              [sg.Listbox(values=ciudades, size=(30, 10), key='ciudades')],
              [sg.Button('Mostrar Pronóstico'), sg.Button('Mostrar Mapa'), sg.Button('Salir')]]

    window = sg.Window('Mapa del Tiempo', layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Salir':
            break
        elif event == 'Mostrar Pronóstico':
            ciudad_seleccionada = values['ciudades'][0]
            pronostico = obtener_prediccion_meteorologica(ciudad_seleccionada, api_key)
            sg.popup(pronostico)
        elif event == 'Mostrar Mapa':
            plt.figure(figsize=(10, 8))
            mapa = Basemap(projection='merc', resolution='h', area_thresh=0.1,
                           llcrnrlon=-19, llcrnrlat=27, urcrnrlon=5, urcrnrlat=44)

            mapa.drawcountries()
            mapa.drawmapboundary(fill_color='aqua')
            mapa.drawcoastlines()
            mapa.drawparallels(np.arange(27., 45., 2.), labels=[1, 0, 0, 0])
            mapa.drawmeridians(np.arange(-20., 6., 2.), labels=[0, 0, 0, 1])

            for _, ciudad in datos.iterrows():
                x, y = mapa(ciudad['Longitud'], ciudad['Latitud'])
                mapa.plot(x, y, 'ro', markersize=8, label=ciudad['Ciudad'])

            plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
            plt.title('Mapa del Tiempo - España')
            plt.show()

    window.close()

def main():
    # Sustituir 'TU_API_KEY' por la clave de API de WeatherStack
    api_key = 'c3869c395e9ce787effb71f812b24247'

    # Cargar las ciudades desde un archivo de entrada
    archivo_ciudades = 'CiudadesLatLong.csv'
    datos_ciudades = obtener_datos_ciudades_desde_archivo(archivo_ciudades)

    if datos_ciudades.empty:
        print("No se encontraron ciudades en el archivo.")
        return

    dibujar_mapa(datos_ciudades, api_key)

if __name__ == "__main__":
    main()



