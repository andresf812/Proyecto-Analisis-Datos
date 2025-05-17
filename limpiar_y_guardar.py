# limpiar_y_guardar.py

import pandas as pd
from limpieza import normalizar_dataset

archivo_entrada = 'Zonas.csv'
archivo_salida = 'Zonas_limpio.csv'

print(f"🧼 Cargando datos desde: {archivo_entrada}")
df = pd.read_csv(archivo_entrada, encoding='latin1')
df_limpio = normalizar_dataset(df)

# Guardar usando punto y coma como delimitador para evitar problemas con comas internas
df_limpio.to_csv(archivo_salida, index=False, sep=';', encoding='utf-8')

print(f"✅ Limpieza completada. Archivo guardado como: {archivo_salida}")
