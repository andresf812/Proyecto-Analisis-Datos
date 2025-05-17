#----- Proyecto: Análisis de Datos de Zonas Horarias -----
# Este script realiza un análisis estadístico y visualización de datos de estabilidad de servicio energético
# en diferentes zonas horarias. Se enfoca en la columna 'PROMEDIO DIARIO EN HORAS'.
# 1. Yaneth Berrio, 2. Santiago Quiroga, 3. Jose Luis Giraldo, 4. Sebastián Cortes, 5. Andrés Felipe Gutiérrez

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unidecode import unidecode
from scipy.stats import norm
from Funciones import (
    limpiar_texto,mostrar_promedio, mostrar_mediana, mostrar_varianza,
    mostrar_desviacion_estandar, mostrar_percentiles,
    posicion_percentil, graficar_distribucion_normal, graficar_promedio
)

# --- Carga y limpieza de datos ---
ds = pd.read_csv('Zonas.csv', encoding='utf-8', delimiter=',', thousands=',', decimal='.')


ds.columns = (
    ds.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("á", "a")
    .str.replace("é", "e")
    .str.replace("í", "i")
    .str.replace("ó", "o")
    .str.replace("ú", "u")
    .str.replace("ñ", "n")
)

# Normalizar texto eliminando tildes
ds = ds.applymap(limpiar_texto)

# Reemplazar espacios en blanco por guiones bajos en los textos
for col in ds.select_dtypes(include=['object']).columns:
    ds[col] = ds[col].str.replace(' ', '_')

# --- Caracterización básica ---
print("\n--- Caracterización de Datos ---")
print("Tamaño total de datos (celdas):", ds.size)
print("Valores nulos por columna:\n", ds.isnull().sum())
print("Número de datos no nulos por columna:\n", ds.count())
print("Número de municipios únicos:", ds['id_municipio'].nunique())
print("Número de departamentos únicos:", ds['id_depatamento'].nunique())
print(ds.head())

# Valor máximo de la columna 'PROMEDIO_DIARIO_EN_HORAS'
col_horas = 'promedio_diario_en_horas'
"""
if col_horas in ds.columns:
    valor_maximo = ds[col_horas].max()
    print(f"Valor máximo de '{col_horas}': {valor_maximo:.2f}")"""""

    # Filtrar valores válidos (<= 24 horas) y mayores a 0
df_filtrado = ds[(ds[col_horas] > 0) & (ds[col_horas] <= 24)]


print(f"\n--- Estadísticas para '{col_horas}' (valores <= 24) ---")
mostrar_promedio(df_filtrado, col_horas)
mostrar_mediana(df_filtrado, col_horas)
mostrar_varianza(df_filtrado, col_horas)
mostrar_desviacion_estandar(df_filtrado, col_horas)
mostrar_percentiles(df_filtrado, col_horas)
posicion_percentil(df_filtrado, col_horas, valor=5)

# Graficar solo con datos válidos
graficar_distribucion_normal(df_filtrado, col_horas)

    # Exportar los valores válidos
   # df_filtrado[[col_horas]].to_csv('promedio_diario_horas.csv', index=False)
    #print(f"\nSe exportaron los valores menores o iguales a 24 de la columna '{col_horas}' a 'promedio_diario_horas.csv'.")
#else:
    #print(f"La columna '{col_horas}' no se encuentra en el DataFrame.")
