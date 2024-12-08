import requests
import pandas as pd
from datetime import datetime

# URL de la API de CoinGecko
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

# Parámetros de la solicitud
params = {
    "vs_currency": "usd",
    "days": "200",  # Últimos 2500 días
    "interval": "daily"  # Intervalo de los datos (diario)
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

# Función principal para obtener y guardar los datos
def guardar_datos_bitcoin():
    precios = obtener_datos()
    if precios:
        df = convertir_a_dataframe(precios)
        # Guardar el DataFrame en un archivo CSV
        df.to_csv('bitcoin_historico.csv', index=False)
        print("Datos guardados correctamente.")
    else:
        print("No se obtuvieron datos.")

# Ejecutar el script de forma manual
guardar_datos_bitcoin()
