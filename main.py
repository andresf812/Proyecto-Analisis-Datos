#----- Proyecto: Análisis de Datos de Zonas Horarias -----
# Este script realiza un análisis estadístico y visualización de datos de estabilidad de servicio energético
# en diferentes zonas horarias. Se enfoca en la columna 'PROMEDIO DIARIO EN HORAS'.
# 1. Yaneth Berrio, 2. Santiago Quiroga, 3. Jose Luis Giraldo, 4. Sebastián Cortes, 5. Andrés Felipe Gutiérrez
# main.py
# main.py

# main.py
"""
Proyecto: Análisis de Datos de Zonas Horarias
Autoría: Equipo (Yaneth Berrio, Santiago Quiroga, Jose Luis Giraldo, Sebastián Cortés, Andrés Felipe Gutiérrez)
Descripción:
    • Carga limpia y robusta del dataset Zonas_limpio.csv
    • Estadísticas descriptivas clave
    • Visualizaciones solicitadas (boxplot, histograma, pie, barras, mapa de calor, dispersión, regresión lineal)
    • Manejo de errores: codificación, delimitador, encabezados faltantes
"""
# main.py
"""
Proyecto: Análisis de Datos de Zonas Horarias
Versión: carga adaptable a separadores
"""

import pandas as pd
from limpieza import normalizar_dataset
from estadisticas import (
    mostrar_max, mostrar_min, mostrar_promedio, mostrar_mediana, mostrar_varianza,
    mostrar_desviacion_estandar, mostrar_percentiles, posicion_percentil)
from graficas import (
    graficar_distribucion_normal, graficar_promedio, graficar_boxplot,
    graficar_histograma, graficar_barras_categoria, graficar_matriz_correlacion,
    graficar_dispersion, graficar_regresion_lineal)

# -----------------------------------------------------------------------------
# 1. Carga adaptativa del CSV --------------------------------------------------
# -----------------------------------------------------------------------------

RUTA = "Zonas_limpio.csv"

# intentos con diferentes configuraciones
def cargar_csv(path: str) -> pd.DataFrame:
    # 1) intento estándar ';' + latin1 + engine c
    try:
        df = pd.read_csv(path, sep=';', encoding='latin1')
        if df.shape[1] > 1:
            return df
    except Exception:
        pass
    # 2) mismo pero engine python (tolerante)
    try:
        df = pd.read_csv(path, sep=';', encoding='latin1', engine='python')
        if df.shape[1] > 1:
            return df
    except Exception:
        pass
    # 3) probar coma
    try:
        df = pd.read_csv(path, sep=',', encoding='latin1')
        if df.shape[1] > 1:
            return df
    except Exception:
        pass
    # 4) engine python con coma
    return pd.read_csv(path, sep=',', encoding='latin1', engine='python')

try:
    df = cargar_csv(RUTA)
except FileNotFoundError:
    raise SystemExit(f"❌ No se encontró el archivo {RUTA}.")

# Normalizar encabezados y texto
df = normalizar_dataset(df)

# Renombrar error tipográfico
if 'id_depatamento' in df.columns:
    df = df.rename(columns={'id_depatamento': 'id_departamento'})

print("--- Caracterización de Datos ---")
print("Tamaño total de datos (celdas):", df.size)
print("Valores nulos por columna:", df.isnull().sum())

if 'id_municipio' in df.columns:
    print("Número de municipios únicos:", df['id_municipio'].nunique())
else:
    print("⚠️  Columna 'id_municipio' ausente. Encabezados:", df.columns.tolist())

# -----------------------------------------------------------------------------
# 2. Estadísticas --------------------------------------------------------------
# -----------------------------------------------------------------------------
col_horas = 'promedio_diario_en_horas'
if col_horas not in df.columns:
    raise KeyError(f"No existe '{col_horas}'. Encabezados actuales: {df.columns.tolist()}")

filtro = (df[col_horas] > 0) & (df[col_horas] <= 24)
if filtro.sum() == 0:
    raise ValueError('No hay registros con horas 0<<=24')

df_filtrado = df[filtro]

print(df.columns)

df_filtro_mun = df[(df['id_municipio'] == 27745) & (df['ano_servicio'].between(2022, 2024))]


print(f"--- Estadísticas de '{col_horas} ' ---")
mostrar_max(df_filtro_mun, col_horas)
mostrar_min(df_filtro_mun, col_horas)
mostrar_promedio(df_filtrado, col_horas)
mostrar_mediana(df_filtrado, col_horas)
mostrar_varianza(df_filtrado, col_horas)
mostrar_desviacion_estandar(df_filtrado, col_horas)
mostrar_percentiles(df_filtrado, col_horas)
posicion_percentil(df_filtrado, col_horas, valor=5)

# -----------------------------------------------------------------------------
# 3. Visualizaciones -----------------------------------------------------------
# -----------------------------------------------------------------------------

#graficar_distribucion_normal(df_filtrado, col_horas)
graficar_promedio(df_filtrado, col_horas)
#graficar_promedio(df_filtro_mun, col_horas)
graficar_boxplot(df_filtro_mun, col_horas)
graficar_histograma(df_filtrado, col_horas)
#graficar_barras_categoria(df_filtrado, col_horas)

num_cols = [c for c in ['energia_activa', 'energia_reactiva', 'potencia_maxima', col_horas] if c in df_filtrado.columns]
if len(num_cols) >= 2:
    graficar_matriz_correlacion(df_filtrado, num_cols)
    if {'potencia_maxima', col_horas}.issubset(df_filtrado.columns):
        graficar_dispersion(df_filtrado, 'potencia_maxima', col_horas)
    if {col_horas, 'energia_activa'}.issubset(df_filtrado.columns):
        graficar_regresion_lineal(df_filtrado, col_horas, 'energia_activa')
else:
    print('⚠️  No hay suficientes columnas numéricas para correlación/regresión.')
