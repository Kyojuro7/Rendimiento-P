import pandas as pd

# Ruta del archivo CSV que deseas leer
archivo_csv = 'bitcoin_historico.csv'

# Leer el archivo CSV usando pandas
df = pd.read_csv(archivo_csv)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


# Graficar los datos originales
df.plot()
plt.title("Serie Temporal Original")
plt.show()

# Ajustar el modelo Holt (solo tendencia lineal)
holt_model = ExponentialSmoothing(df['Precio (USD)'], trend='add', seasonal=None)

# Ajustar el modelo con optimización automática
holt_fit = holt_model.fit(optimized=True)

# Mostrar los parámetros ajustados
print(f"Parámetros ajustados: \n{holt_fit.params}")

# Realizar predicciones
forecast = holt_fit.forecast(steps=10)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Precio (USD)'], label='Datos Históricos')
plt.plot(pd.date_range(df.index[-1], periods=11, freq='D')[1:], forecast, label='Predicción Holt', color='red')
plt.legend()
plt.title("Predicción con Holt's Linear Trend")
plt.show()
