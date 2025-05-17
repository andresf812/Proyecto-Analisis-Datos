import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def limpiar_texto(valor):
    if isinstance(valor, str):
        return (
            valor.strip()
            .lower()
            .replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
            .replace("ñ", "n")
        )
    return valor
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

def graficar_distribucion_normal(df, col):
    datos = df[col].dropna()
    media = datos.mean()
    std = datos.std()


    plt.figure(figsize=(10, 6))
    plt.hist(datos, bins=30, density=True, alpha=0.6, color='skyblue', label='Datos')
    
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, media, std)
    plt.plot(x, p, 'r', linewidth=2, label='Distribución Normal')
    
    plt.title(f'Distribución de {col}')
    plt.xlabel(col)
    plt.ylabel('Densidad')
    plt.legend()
    plt.grid(True)
    plt.show()

    def graficar_promedio(df, col):
        plt.figure(figsize=(10, 6))
        plt.plot(df[col], marker='o', linestyle='-', color='blue')
        plt.title(f'Promedio de {col}')
        plt.xlabel('Índice')
        plt.ylabel(col)
        plt.grid(True)
        plt.show()
