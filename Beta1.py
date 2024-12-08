import requests
import pandas as pd
from datetime import datetime, timedelta
import os

# Define la URL de la API de CoinGecko para obtener datos históricos de Bitcoin
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

# Define los parámetros de la solicitud
params = {
    "vs_currency": "usd",  # Moneda en la que se desean los datos
    "days": "2500",          # Todos los datos disponibles hasta el momento
    "interval": "daily"     # Intervalo de los datos (diario)
}

# Función para realizar la llamada a la API
def obtener_datos():
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        precios = data.get("prices", [])
        return precios
    else:
        print(f"Error al obtener los datos: {response.status_code}")
        return None

# Función para convertir los datos a un DataFrame con fechas legibles
def convertir_a_dataframe(precios):
    # Convertir las marcas de tiempo a formato legible
    fechas = [datetime.utcfromtimestamp(item[0] / 1000).strftime('%Y-%m-%d') for item in precios]
    valores = [item[1] for item in precios]
    
    # Crear un DataFrame
    df = pd.DataFrame({
        'Fecha': fechas,
        'Precio (USD)': valores
    })
    
    return df

# Función principal que solo ejecuta una llamada al día
def ejecutar_una_vez_al_dia():
    # Verifica si ya pasó un día desde la última ejecución
    archivo_fecha = 'ultima_ejecucion.txt'
    
    if os.path.exists(archivo_fecha):
        with open(archivo_fecha, 'r') as file:
            ultima_ejecucion = file.read()
            ultima_ejecucion = datetime.strptime(ultima_ejecucion, "%Y-%m-%d %H:%M:%S")
    else:
        ultima_ejecucion = None

    # Si no se ha ejecutado hoy, ejecuta la llamada
    if ultima_ejecucion is None or (datetime.now() - ultima_ejecucion).days >= 1:
        print("Ejecutando la llamada a la API...")

        # Obtener los datos de la API
        precios = obtener_datos()
        if precios:
            # Convertir los datos a DataFrame
            df = convertir_a_dataframe(precios)
            print(df.head())  # Mostrar las primeras filas para verificar

            # Guardar la fecha y hora de la última ejecución
            with open(archivo_fecha, 'w') as file:
                file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            print("No se obtuvieron datos.")
    else:
        print("Ya se ha ejecutado hoy. Esperando hasta mañana.")

# Ejecutar la función
ejecutar_una_vez_al_dia()
