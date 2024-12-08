import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Ruta del archivo Excel
archivo = r'C:\Users\B Josue AS\Documents\Universidad\Estadistica\Regresion Lineal\Trabajo Final\Datos 5.7.xlsx'

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel(archivo)

# Datos independientes (características)
independ = df[["Cores", "Frequency", "Cache L3", "Temperatura"]]

# Variable dependiente (objetivo)
depend = df["Benchmarks"]

# Crear el modelo de regresión lineal
mod = LinearRegression()

# Ajustar el modelo con las variables independientes (X) y la dependiente (y)
mod.fit(independ, depend)

pred = mod.predict(independ)

plt.scatter(depend, pred, color='blue', label='Predicciones')
plt.plot([min(depend), max(depend)], [min(depend), max(depend)], color='red', label='Línea de ajuste')
plt.title("Predicciones vs Valores Reales")
plt.xlabel("Valores Reales (Benchmarks)")
plt.ylabel("Predicciones")
plt.legend()
#plt.show()

# Guardar el modelo y los coeficientes
print(mod.coef_)
print(mod.intercept_)
