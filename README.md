# Mapa del Tiempo - España

Este programa utiliza la API de WeatherStack para obtener información meteorológica de diversas ciudades en España y visualiza los datos de temperatura, descripción del clima y velocidad del viento a través de un mapa interactivo.

## Requisitos

- Python 3.x
- Clave de API de WeatherStack (Sustituir 'TU_API_KEY' en el código con tu clave de API válida).
- Para obtener esta clave API debes registrarte en la pagina https://weatherstack.com/dashboard.
- Bibliotecas necesarias (puedes instalarlas con `pip install numpy requests PySimpleGUI matplotlib pandas`).
## Uso

1. Ejecuta el script en un entorno que admita la interfaz gráfica de PySimpleGUI.
2. Selecciona una ciudad desde la lista desplegable.
3. Haz clic en "Mostrar Pronóstico" para ver una ventana emergente con el pronóstico detallado de la ciudad seleccionada.
4. Haz clic en "Mostrar Mapa" para visualizar un mapa interactivo con marcadores que representan las ciudades. Al hacer clic en un marcador, se mostrará un mensaje emergente con el pronóstico de la ciudad correspondiente.
5. Cierra la aplicación cuando hayas terminado.

## Estructura del Código

- **obtener_prediccion_meteorologica:** Función para obtener el pronóstico meteorológico de una ciudad.
- **obtener_datos_ciudades_desde_archivo:** Función para cargar datos de ciudades desde un archivo CSV.
- **dibujar_mapa:** Función principal para dibujar el mapa interactivo.
- **main:** Función principal para ejecutar el programa.

## Bibliotecas Utilizadas

- `numpy`: Para operaciones numéricas.
- `requests`: Para realizar solicitudes a la API de WeatherStack.
- `PySimpleGUI`: Para la interfaz gráfica.
- `matplotlib`: Para crear visualizaciones y mapas.
- `pandas`: Para la manipulación de datos.

## Importante

Asegúrate de tener una conexión a Internet activa para obtener datos meteorológicos en tiempo real. Además, utiliza un entorno de escritorio para una experiencia completa con la interfaz gráfica.


## Autor
Este trabajo ha sido realizado por Hector Pesquera Rodriguez.
