import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(page_title="Predicción de Rendimiento en Benchmark", page_icon=":computer:", layout="wide")

# Título y descripción
st.title("Predicción de Rendimiento en Benchmark de tu Procesador")

st.write("""
Bienvenido a nuestra aplicación de predicción de rendimiento en benchmark de procesadores. 
¿Alguna vez te has preguntado qué tan bien podría funcionar tu procesador en tareas exigentes como videojuegos, edición de video o simulaciones? 

Con esta herramienta, puedes predecir el rendimiento de tu procesador basándote en sus componentes principales de este.

### ¿Cómo funciona?
1. **Ingresa los detalles de tu procesador**: Completa la información de los componentes de tu procesador.
2. **Predicción del rendimiento**: Nuestra aplicación utilizará los datos ingresados para predecir el rendimiento de tu procesador en benchmarks típicos.
3. **Resultados y recomendaciones**: Obtén una estimación sobre el rendimiento de tu procesador y sugerencias de mejora, si es necesario.

**¡Comienza ahora!** Ingresa los detalles de tu procesador para ver cómo se desempeñaría en pruebas de benchmark.
         
### Ingresa las características de tu procesador.
""")

# Crear 4 columnas con anchos relativos
col1, col2, col3, col4 = st.columns(4)

# Caja para ingresar el número de Cores
with col1:
    cores = st.number_input("Ingresa el número de Cores", min_value=1.0, max_value=64.0, step=1.0)

# Caja para ingresar la frecuencia (Frequency)
with col2:
    frequency = st.number_input("Ingresa la frecuencia (GHz)", min_value=0.01, max_value=7.0, step=0.1)

# Caja para ingresar el tamaño de la caché L3 (Cache L3)
with col3:
    cache_l3 = st.number_input("Ingresa el tamaño de Cache L3 (MB)", min_value=1.0, max_value=128.0,  step=1.0)

# Caja para ingresar la temperatura (Temperatura)
with col4:
    temperatura = st.number_input("Ingresa la temperatura (°C)", min_value=20.0, max_value=100.0, step=0.1)

# Validación: comprobar si todos los valores son mayores que cero
if cores <= 0 or frequency <= 0 or cache_l3 <= 0 or temperatura <= 0:
    st.error("Por favor, ingresa valores válidos (mayores que cero) para todas las características.")

ren = -42132.4365 + cores * 1950.00828555 + frequency * 4523.4741 + cache_l3 * 152.2956 + temperatura * 313.2721


# Almacenar los datos en un dataframe
data = {
    "Cores": [cores],
    "Frequency": [frequency],
    "Cache L3": [cache_l3],
    "Temperatura": [temperatura]
}

dfg = pd.DataFrame(data)

# Guardar los datos en el archivo CSV automáticamente
dfg.to_csv('datos_usuarios.csv', mode='a', header=False, index=False)

st.write(f"### El rendimiento de tu procesador en benchmarks sería: {round(ren, 4)}")

st.write("""### Justificación
En los gráficos de dispersión que muestran la relación entre los benchmarks y las variables independientes,
como el número de cores, la frecuencia, el tamaño de la caché L3 y la temperatura, se observa una tendencia
lineal en los datos. Esto sugiere que a medida que estas características del hardware de la computadora cambian,
el rendimiento de los benchmarks también muestra un patrón de variación consistente, lo que podría indicar que 
estas variables influyen de manera significativa en el rendimiento general del sistema. El análisis de estos 
gráficos puede ser útil para entender cómo la configuración del hardware afecta el desempeño en tareas de 
benchmarking y podría ser un punto de partida para mejorar el rendimiento mediante la optimización de estas
características clave.
""")


# Ruta del archivo Excel
archivo = "Datos 5.7.xlsx"

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel(archivo)

# Datos independientes (características)
df = df[["Benchmarks", "Cores", "Frequency", "Cache L3", "Temperatura"]]

col1, col2 = st.columns(2)

with col1:
    # Crear gráfico de dispersión interactivo con Plotly
    fig1 = px.scatter(df, x='Cores', y='Benchmarks',
                 title="Benchmarks vs Cores",
                 labels={'Cores': 'Número de Cores', 'Benchmarks': 'Puntuación de Benchmarks'})
    st.plotly_chart(fig1)

with col2:
    # Crear gráfico de dispersión interactivo con Plotly
    fig2 = px.scatter(df, x='Frequency', y='Benchmarks',
                 title="Benchmarks vs Frequency",
                 labels={'Frequency': 'Frequencia', 'Benchmarks': 'Puntuación de Benchmarks'})
    st.plotly_chart(fig2)

with col1:
    # Crear gráfico de dispersión interactivo con Plotly
    fig3 = px.scatter(df, x="Cache L3", y='Benchmarks',
                 title="Benchmarks vs Cache L3",
                 labels={'Cache L3': 'Cache L3', 'Benchmarks': 'Puntuación de Benchmarks'})
    st.plotly_chart(fig3)

with col2:
    # Crear gráfico de dispersión interactivo con Plotly
    fig4 = px.scatter(df, x="Temperatura", y='Benchmarks',
                 title="Benchmarks vs Temperatura",
                 labels={'Temperatura': 'Temperatura', 'Benchmarks': 'Puntuación de Benchmarks'})
    st.plotly_chart(fig4)

# streamlit run pagweb.py

#x=[1950.00828555 4523.47415509  152.29562929  313.27218355]
#-42132.436579897505
#y=-42132.4365+1950.0082*x

st.write("Ten en cuenta que los datos que ingreses en esta herramienta serán almacenados de manera segura para su análisis y mejora continua del modelo predictivo. Nos aseguramos de que la información se gestione respetando la privacidad y confidencialidad de los usuarios, utilizándola exclusivamente con fines de investigación y optimización. Si tienes alguna inquietud respecto al manejo de tus datos, no dudes en contactarnos.")
