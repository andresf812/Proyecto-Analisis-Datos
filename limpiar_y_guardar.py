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

# Guardar archivo limpio
df_limpio.to_csv(archivo_salida, index=False, encoding='utf-8')

print(f"\n✅ Limpieza completada. Archivo guardado como: {archivo_salida}")
