# graficas.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import norm, linregress


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


def graficar_regresion_lineal_por_municipio(
        df: pd.DataFrame,
        x_col: str = "ano_servicio",
        y_col: str = "promedio_diario_en_horas",
        municipio_col: str = "municipio",
        *,
        min_puntos: int = 3,
        top_n_lowest: int | None = None,          # ⬅️  nuevo
        municipios_a_mostrar: list[str] | None = None,
        guardar: bool = True,
        nombre_archivo: str | None = None,
) -> None:
    """
    Dibuja la regresión lineal Y vs X para cada municipio seleccionado.
    Si `top_n_lowest` se proporciona, se grafican únicamente los N municipios
    con menor promedio en `y_col`.

    Otros parámetros idénticos a la versión anterior.
    """

    # ────────── 1. Selección automática de municipios “críticos” ──────────
    if top_n_lowest is not None:
        promedios = (df.groupby(municipio_col)[y_col]
                     .mean()
                     .sort_values()
                     .head(top_n_lowest))
        municipios_iter = promedios.index.tolist()
    elif municipios_a_mostrar is not None:
        municipios_iter = municipios_a_mostrar
    else:
        municipios_iter = df[municipio_col].unique()

    # ────────── 2. Gráfico base ───────────────────────────────────────────
    plt.figure(figsize=(10, 7))

    for mpio in municipios_iter:
        datos = df[df[municipio_col] == mpio][[x_col, y_col]].dropna()
        if len(datos) < min_puntos:
            continue
        x_vals = datos[x_col].values
        y_vals = datos[y_col].values
        if np.unique(x_vals).size < 2:
            continue

        slope, intercept, *_ = linregress(x_vals, y_vals)

        plt.scatter(x_vals, y_vals, alpha=0.6, label=f"{mpio} (β={slope:.2f})")
        x_line = np.linspace(x_vals.min(), x_vals.max(), 100)
        plt.plot(x_line, slope * x_line + intercept)

    # ────────── 3. Etiquetas, guardado o visualización ───────────────────
    plt.xlabel(x_col.replace("_", " ").title())
    plt.ylabel(y_col.replace("_", " ").title())
    plt.title(f"Regresión lineal de {y_col} vs {x_col}\n"
              f"(Top {top_n_lowest} municipios con menor promedio)" if top_n_lowest
              else f"Regresión lineal de {y_col} vs {x_col} por municipio")
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", fontsize=7)

    # Mostrar años como enteros en el eje X si corresponde
    if x_col in ["ano_servicio", "año_servicio", "anio", "ano"]:
        todos_los_anos = sorted(set(df[x_col].dropna().astype(int)))
        plt.xticks(todos_los_anos, [str(a) for a in todos_los_anos])

    plt.tight_layout()

    if guardar:
        if nombre_archivo is None:
            sufijo = f"_top{top_n_lowest}" if top_n_lowest else ""
            nombre_archivo = (f"regresion_lineal_{y_col}_vs_{x_col}"
                              f"_por_municipio{sufijo}.png")
        plt.savefig(nombre_archivo, dpi=150, bbox_inches="tight")
        print(f"✅ Gráfica guardada como '{nombre_archivo}'")
    else:
        plt.show()