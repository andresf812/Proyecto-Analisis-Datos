# graficas.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import norm, linregress

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
    valores = df[col].value_counts().head(10)
    etiquetas = valores.index.astype(str)

    plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribución de {col} (Top 10 valores)')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(f'{col}_pie.png')
    print(f"✅ Gráfica guardada como '{col}_pie.png'")

def graficar_boxplot(df, col):
    plt.figure(figsize=(10, 6))
    plt.boxplot(df[col].dropna(), vert=False)
    plt.title(f'Boxplot de {col}')
    plt.xlabel(col)
    plt.grid(True)
    plt.savefig(f'{col}_boxplot.png')
    print(f"✅ Gráfica guardada como '{col}_boxplot.png'")

def graficar_histograma(df, col):
    plt.figure(figsize=(8, 5))
    plt.hist(df[col].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histograma de {col}')
    plt.xlabel(col)
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.savefig(f'{col}_histograma.png')
    print(f"✅ Histograma guardado como '{col}_histograma.png'")

def graficar_barras_categoria(df, col):
    categorias = pd.cut(df[col], bins=[0, 8, 16, 24], labels=["Baja", "Media", "Alta"])
    conteo = categorias.value_counts().sort_index()
    plt.figure(figsize=(8, 6))
    conteo.plot(kind='bar', color=['red', 'orange', 'green'])
    plt.title(f'Disponibilidad de {col} por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Cantidad')
    plt.grid(True)
    plt.savefig(f'{col}_barras_categoria.png')
    print(f"✅ Barras guardadas como '{col}_barras_categoria.png'")

def graficar_matriz_correlacion(df, cols):
    plt.figure(figsize=(8, 6))
    corr = df[cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Matriz de Correlación')
    plt.savefig('matriz_correlacion.png')
    print("✅ Mapa de calor guardado como 'matriz_correlacion.png'")

def graficar_dispersion(df, x_col, y_col):
    plt.figure(figsize=(8, 6))
    plt.scatter(df[x_col], df[y_col], alpha=0.6)
    plt.title(f'Dispersión entre {x_col} y {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.savefig(f'dispersion_{x_col}_vs_{y_col}.png')
    print(f"✅ Dispersión guardada como 'dispersion_{x_col}_vs_{y_col}.png'")

def graficar_regresion_lineal(df, x_col, y_col):
    x = df[x_col].dropna()
    y = df[y_col].dropna()
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.6, label='Datos')
    plt.plot(x, slope * x + intercept, 'r', label=f'Regresión: y={slope:.2f}x+{intercept:.2f}')
    plt.title(f'Regresión Lineal: {x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.grid(True)
    plt.savefig(f'regresion_{x_col}_vs_{y_col}.png')
    print(f"✅ Regressión lineal guardada como 'regresion_{x_col}_vs_{y_col}.png'")
