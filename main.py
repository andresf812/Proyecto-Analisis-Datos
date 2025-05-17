# main.py

import pandas as pd
from estadisticas import (
    mostrar_promedio, mostrar_mediana, mostrar_varianza,
    mostrar_desviacion_estandar, mostrar_percentiles,
    posicion_percentil, graficar_distribucion_normal, graficar_promedio
)

# Archivo limpio generado previamente por 'limpiar_y_guardar.py'
archivo_limpio = 'Zonas_limpio.csv'

# Cargar datos ya limpios
df = pd.read_csv(archivo_limpio)

# Mostrar características básicas
print("\n--- Caracterización de Datos ---")
print("Tamaño total de datos (celdas):", df.size)
print("Valores nulos por columna:\n", df.isnull().sum())
print("Número de municipios únicos:", df["id_municipio"].nunique())

# Columna objetivo
col_horas = "promedio_diario_en_horas"

# Filtrar valores válidos (entre 0 y 24 horas)
df_filtrado = df[(df[col_horas] > 0) & (df[col_horas] <= 24)]

# Estadísticas descriptivas
print(f"\n--- Estadísticas para '{col_horas}' ---")
mostrar_promedio(df_filtrado, col_horas)
mostrar_mediana(df_filtrado, col_horas)
mostrar_varianza(df_filtrado, col_horas)
mostrar_desviacion_estandar(df_filtrado, col_horas)
mostrar_percentiles(df_filtrado, col_horas)
posicion_percentil(df_filtrado, col_horas, valor=5)

# Visualizaciones
graficar_distribucion_normal(df_filtrado, col_horas)
graficar_promedio(df_filtrado, col_horas)
