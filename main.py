#----- Proyecto: Análisis de Datos de Zonas Horarias -----
# Este script realiza un análisis estadístico y visualización de datos de estabilidad de servicio energético
# en diferentes zonas horarias. Se enfoca en la columna 'PROMEDIO DIARIO EN HORAS'.
# 1. Yaneth Berrio, 2. Santiago Quiroga, 3. Jose Luis Giraldo, 4. Sebastián Cortes, 5. Andrés Felipe Gutiérrez

import pandas as pd
from estadisticas import (
    mostrar_promedio, mostrar_mediana, mostrar_varianza,
    mostrar_desviacion_estandar, mostrar_percentiles,
    posicion_percentil
)
from graficas import (
    graficar_distribucion_normal, graficar_promedio
)

# Cargar datos limpios
df = pd.read_csv("Zonas_limpio.csv")

print("\n--- Caracterización de Datos ---")
print("Tamaño total de datos (celdas):", df.size)
print("Valores nulos por columna:\n", df.isnull().sum())
print("Número de municipios únicos:", df["id_municipio"].nunique())

col_horas = "promedio_diario_en_horas"
df_filtrado = df[(df[col_horas] > 0) & (df[col_horas] <= 24)]

# Estadísticas
print(f"\n--- Estadísticas para '{col_horas}' ---")
mostrar_promedio(df_filtrado, col_horas)
mostrar_mediana(df_filtrado, col_horas)
mostrar_varianza(df_filtrado, col_horas)
mostrar_desviacion_estandar(df_filtrado, col_horas)
mostrar_percentiles(df_filtrado, col_horas)
posicion_percentil(df_filtrado, col_horas, valor=5)

# Gráficas
graficar_distribucion_normal(df_filtrado, col_horas)
graficar_promedio(df_filtrado, col_horas)
