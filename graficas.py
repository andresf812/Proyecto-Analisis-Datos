# graficas.py

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def graficar_distribucion_normal(df, col):
    datos = df[col].dropna()
    media = datos.mean()
    std = datos.std()

    plt.figure(figsize=(10, 6))
    plt.hist(datos, bins=30, density=True, alpha=0.6, color='skyblue', label='Datos')
    x = np.linspace(datos.min(), datos.max(), 100)
    p = norm.pdf(x, media, std)
    plt.plot(x, p, 'r', linewidth=2, label='Distribución Normal')
    plt.title(f'Distribución de {col}')
    plt.xlabel(col)
    plt.ylabel('Densidad')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{col}_distribucion.png')
    print(f"✅ Gráfica guardada como '{col}_distribucion.png'")

def graficar_promedio(df, col):
    plt.figure(figsize=(8, 8))
    valores = df[col].value_counts().head(10)  # Tomamos los 10 valores más frecuentes (puedes ajustar esto)
    etiquetas = valores.index.astype(str)

    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribución de {col} (Top 10 valores)')
    plt.axis('equal')  # Mantener la proporción circular
    plt.tight_layout()
    plt.show()
