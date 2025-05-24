# graficas.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import norm, linregress

# def graficar_diagrama_dispersion(df, col):
#     datos = df[col].dropna()
#     media = datos.mean()
#     std = datos.std()

#     plt.figure(figsize=(10, 6))
#     plt.hist(datos, bins=30, density=True, alpha=0.6, color='skyblue', label='Datos')
#     x = np.linspace(datos.min(), datos.max(), 100)
#     p = norm.pdf(x, media, std)
#     plt.plot(x, p, 'r', linewidth=2, label='Distribución Normal')
#     plt.title(f'Distribución de {col}')
#     plt.xlabel(col)
#     plt.ylabel('Densidad')
#     plt.legend()
#     plt.grid(True)
#     plt.savefig(f'{col}_distribucion.png')
#     print(f"✅ Gráfica guardada como '{col}_distribucion.png'")

# def graficar_pie(df, col):
#     plt.figure(figsize=(8, 8))
#     valores = df[col].value_counts().head(10)
#     etiquetas = valores.index.astype(str)

#     plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140)
#     plt.title(f'Distribución de {col} (Top 10 valores)')
#     plt.axis('equal')
#     plt.tight_layout()
#     plt.savefig(f'{col}_pie.png')
#     print(f"✅ Gráfica guardada como '{col}_pie.png'")

# def graficar_boxplot(df, col):
#     plt.figure(figsize=(10, 6))
#     plt.boxplot(df[col].dropna(), vert=False)
#     plt.title(f'Boxplot de {col}')
#     plt.xlabel(col)
#     plt.grid(True)
#     plt.savefig(f'{col}_boxplot.png')
#     print(f"✅ Gráfica guardada como '{col}_boxplot.png'")

# def graficar_histograma(df, col):
#     plt.figure(figsize=(8, 5))
#     plt.hist(df[col].dropna(), bins=20, color='skyblue', edgecolor='black')
#     plt.title(f'Histograma de {col}')
#     plt.xlabel(col)
#     plt.ylabel('Frecuencia')
#     plt.grid(True)
#     plt.savefig(f'{col}_histograma.png')
#     print(f"✅ Histograma guardado como '{col}_histograma.png'")

# def graficar_barras_categoria(df, col):
#     categorias = pd.cut(df[col], bins=[0, 8, 16, 24], labels=["Baja", "Media", "Alta"])
#     conteo = categorias.value_counts().sort_index()
#     plt.figure(figsize=(8, 6))
#     conteo.plot(kind='bar', color=['red', 'orange', 'green'])
#     plt.title(f'Disponibilidad de {col} por Categoría')
#     plt.xlabel('Categoría')
#     plt.ylabel('Cantidad')
#     plt.grid(True)
#     plt.savefig(f'{col}_barras_categoria.png')
#     print(f"✅ Barras guardadas como '{col}_barras_categoria.png'")

# def graficar_matriz_correlacion(df, cols):
#     plt.figure(figsize=(8, 6))
#     corr = df[cols].corr()
#     sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
#     plt.title('Matriz de Correlación')
#     plt.savefig('matriz_correlacion.png')
#     print("✅ Mapa de calor guardado como 'matriz_correlacion.png'")

# def graficar_dispersion(df, x_col, y_col):
#     plt.figure(figsize=(8, 6))
#     plt.scatter(df[x_col], df[y_col], alpha=0.6)
#     plt.title(f'Dispersión entre {x_col} y {y_col}')
#     plt.xlabel(x_col)
#     plt.ylabel(y_col)
#     plt.grid(True)
#     plt.savefig(f'dispersion_{x_col}_vs_{y_col}.png')
#     print(f"✅ Dispersión guardada como 'dispersion_{x_col}_vs_{y_col}.png'")

# def graficar_regresion_lineal(df, x_col, y_col):
#     x = df[x_col].dropna()
#     y = df[y_col].dropna()
#     slope, intercept, r_value, p_value, std_err = linregress(x, y)

#     plt.figure(figsize=(8, 6))
#     plt.scatter(x, y, alpha=0.6, label='Datos')
#     plt.plot(x, slope * x + intercept, 'r', label=f'Regresión: y={slope:.2f}x+{intercept:.2f}')
#     plt.title(f'Regresión Lineal: {x_col} vs {y_col}')
#     plt.xlabel(x_col)
#     plt.ylabel(y_col)
#     plt.legend()
#     plt.grid(True)
#     plt.savefig(f'regresion_{x_col}_vs_{y_col}.png')
#     print(f"✅ Regressión lineal guardada como 'regresion_{x_col}_vs_{y_col}.png'")

def graficar_barras_promedio_municipio(df, col_horas, col_municipio):
    promedios = df.groupby(col_municipio)[col_horas].mean().sort_values()
    plt.figure(figsize=(12, 6))
    promedios.plot(kind='bar', color='skyblue')
    plt.title(f'Promedio de {col_horas} por municipio')
    plt.xlabel('Municipio')
    plt.ylabel(f'Promedio de {col_horas}')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'promedio_{col_horas}_por_municipio.png')
    print(f"✅ Gráfica guardada como 'promedio_{col_horas}_por_municipio.png'")

def graficar_boxplot_promedio_municipio(df, col_horas, col_municipio):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x=col_municipio, y=col_horas, data=df)
    plt.title(f'Boxplot de {col_horas} por municipio')
    plt.xlabel('Municipio')
    plt.ylabel(f'{col_horas}')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'boxplot_{col_horas}_por_municipio.png')
    print(f"✅ Gráfica guardada como 'boxplot_{col_horas}_por_municipio.png'")

def graficar_violin_promedio_municipio(df, col_horas, col_municipio):
    plt.figure(figsize=(12, 6))
    sns.violinplot(x=col_municipio, y=col_horas, data=df)
    plt.title(f'Violin plot de {col_horas} por municipio')
    plt.xlabel('Municipio')
    plt.ylabel(f'{col_horas}')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'violin_{col_horas}_por_municipio.png')
    print(f"✅ Gráfica guardada como 'violin_{col_horas}_por_municipio.png'")

def graficar_diagrama_dispersion(df, col_x, col_y):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[col_x], df[col_y], alpha=0.7, color='teal')
    plt.title(f'Diagrama de dispersión: {col_x} vs {col_y}')
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'dispersion_{col_x}_vs_{col_y}.png')
    print(f"✅ Gráfica guardada como 'dispersion_{col_x}_vs_{col_y}.png'")

def graficar_promedio_pie_municipio(df, col_horas, col_municipio):
    promedios = df.groupby(col_municipio)[col_horas].mean().sort_values(ascending=False)
    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(promedios, labels=None, autopct='%1.1f%%', startangle=140)
    plt.title(f'Promedio de {col_horas} por municipio')
    plt.axis('equal')
    plt.tight_layout()
    plt.legend(wedges, promedios.index, title="Municipio", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.savefig(f'promedio_{col_horas}_pie_municipio.png', bbox_inches='tight')
    print(f"✅ Gráfica guardada como 'promedio_{col_horas}_pie_municipio.png'")

def graficar_promedio_histograma_municipio_anio(df, col_horas, col_municipio, col_anio):
    promedios = df.groupby([col_municipio, col_anio])[col_horas].mean()
    plt.figure(figsize=(8, 6))
    plt.hist(promedios, bins=10, color='skyblue', edgecolor='black')
    plt.title(f'Histograma del promedio de {col_horas} por municipio y año')
    plt.xlabel(f'Promedio de {col_horas}')
    plt.ylabel('Cantidad de municipio-año')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'histograma_promedio_{col_horas}_por_municipio_anio.png')
    print(f"✅ Histograma guardado como 'histograma_promedio_{col_horas}_por_municipio_anio.png'")

# def graficar_promedio_histograma_anio(df, col_anio, col_horas):
#     promedios = df.groupby(col_anio)[col_horas].mean()
#     plt.figure(figsize=(8, 6))
#     plt.hist(promedios, bins=len(promedios), color='skyblue', edgecolor='black')
#     plt.title(f'Histograma del promedio de {col_horas} por año')
#     plt.xlabel(f'Promedio de {col_horas}')
#     plt.ylabel('Cantidad de años')
#     plt.grid(True)
#     plt.tight_layout()
#     plt.savefig(f'histograma_promedio_{col_horas}_por_anio.png')
#     print(f"✅ Histograma guardado como 'histograma_promedio_{col_horas}_por_anio.png'")

def graficar_histograma_anio(df, col_horas, col_anio):
    promedios = df.groupby(col_anio)[col_horas].mean()
    plt.figure(figsize=(8, 6))
    plt.bar(promedios.index.astype(int), promedios.values, color='skyblue', edgecolor='black')
    plt.title(f'Promedio de {col_horas} por año')
    plt.xlabel('Año')
    plt.ylabel(f'Promedio de {col_horas}')
    plt.xticks(promedios.index.astype(int))
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig(f'histograma_{col_horas}_por_anio.png')
    print(f"✅ Gráfica guardada como 'promedio_histograma_{col_horas}_por_anio.png'")

def graficar_regresion_lineal_por_municipio(df, x_col, y_col, municipio_col, top_n=10, min_puntos=3):
    municipios = df[municipio_col].unique()
    plt.figure(figsize=(10, 7))
    for municipio in municipios:
        datos = df[df[municipio_col] == municipio][[x_col, y_col]].dropna()
        if len(datos) < min_puntos:
            continue
        x = datos[x_col]
        y = datos[y_col]
        slope, intercept, _, _, _ = linregress(x, y)
        plt.scatter(x, y, label=f"{municipio}", alpha=0.5)
        # Para que la línea cubra todo el rango de x de ese municipio:
        x_line = np.linspace(x.min(), x.max(), 100)
        y_line = slope * x_line + intercept
        plt.plot(x_line, y_line)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Regresión lineal de {y_col} vs {x_col} por municipio")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f'regresion_lineal_{y_col}_vs_{x_col}_por_municipio.png', bbox_inches='tight')
    print(f"✅ Gráfica guardada como 'regresion_lineal_{y_col}_vs_{x_col}_por_municipio.png'")

    # --- Top N municipios con menor promedio diario en horas ---
    if x_col == "promedio_diario_en_horas" and top_n > 0:
        promedios = df.groupby(municipio_col)[x_col].mean().sort_values().head(top_n)
        plt.figure(figsize=(10, 6))
        promedios.plot(kind='bar', color='tomato')
        plt.title(f'Top {top_n} municipios con menor promedio diario en horas')
        plt.xlabel('Municipio')
        plt.ylabel('Promedio diario en horas')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f'top{top_n}_municipios_menor_promedio_diario_en_horas.png')
        print(f"✅ Gráfica guardada como 'top{top_n}_municipios_menor_promedio_diario_en_horas.png'")
