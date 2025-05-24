# limpiar_y_guardar.py

import pandas as pd
from limpieza import normalizar_dataset

# Cargar archivo original
archivo_entrada = 'Zonas.csv'
archivo_salida = 'Zonas_limpio.csv'

print(f"Cargando datos desde: {archivo_entrada}")
df = pd.read_csv( archivo_entrada , encoding='utf-8', delimiter=',', thousands=',', decimal='.')

# Aplicar limpieza
df_limpio = normalizar_dataset(df)

# Asegurar que el campo año_servicio sea entero
if 'ano_servicio' in df_limpio.columns:
    df_limpio['ano_servicio'] = pd.to_numeric(df_limpio['ano_servicio'], errors='coerce')
    df_limpio = df_limpio[df_limpio['ano_servicio'].notna()]
    df_limpio['ano_servicio'] = df_limpio['ano_servicio'].astype(int)

# Guardar archivo limpio
df_limpio.to_csv(archivo_salida, index=False, encoding='utf-8')

print(f"\n✅ Limpieza completada. Archivo guardado como: {archivo_salida}")
