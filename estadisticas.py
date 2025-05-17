# estadisticas.py

import numpy as np

def mostrar_promedio(df, col):
    valor = df[col].mean()
    print(f"Promedio: {valor:.2f}")
    return valor

def mostrar_mediana(df, col):
    valor = df[col].median()
    print(f"Mediana: {valor:.2f}")
    return valor

def mostrar_varianza(df, col):
    valor = df[col].var()
    print(f"Varianza: {valor:.2f}")
    return valor

def mostrar_desviacion_estandar(df, col):
    valor = df[col].std()
    print(f"Desviación estándar: {valor:.2f}")
    return valor

def mostrar_percentiles(df, col, percentiles=[25, 50, 75, 90]):
    print(f"\nPercentiles de '{col}':")
    for p in percentiles:
        val = np.percentile(df[col].dropna(), p)
        print(f"  Percentil {p}%: {val:.2f}")
    return

def posicion_percentil(df, col, valor):
    datos = df[col].dropna().sort_values().reset_index(drop=True)
    posicion = (datos < valor).sum() / len(datos) * 100
    print(f"\nEl valor {valor:.2f} está en aproximadamente el percentil {posicion:.2f}")
    return posicion
