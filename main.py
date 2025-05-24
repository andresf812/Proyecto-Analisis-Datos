#----- Proyecto: Análisis de Datos de Zonas Horarias -----
# Este script realiza un análisis estadístico y visualización de datos de estabilidad de servicio energético
# en diferentes zonas horarias. Se enfoca en la columna 'PROMEDIO DIARIO EN HORAS'.
# 1. Yaneth Berrio, 2. Santiago Quiroga, 3. Jose Luis Giraldo, 4. Sebastián Cortes, 5. Andrés Felipe Gutiérrez
# main.py
"""
Proyecto: Análisis de Datos de Zonas Horarias – Filtro dinámico + Descripción
Permite filtrar por ID de municipio (M) o ID de departamento (D) y generar
estadísticas + gráficas para el subconjunto elegido. Además, solicita una
breve descripción que se muestra antes de los resultados.
"""

import pandas as pd
from limpieza import normalizar_dataset
from estadisticas import (
    mostrar_promedio, mostrar_mediana, mostrar_varianza,
    mostrar_desviacion_estandar, mostrar_percentiles, posicion_percentil)
from graficas import (
    graficar_distribucion_normal, graficar_promedio, graficar_boxplot,
    graficar_histograma, graficar_barras_categoria, graficar_matriz_correlacion,
    graficar_dispersion, graficar_regresion_lineal)

RUTA = "Zonas_limpio.csv"

# --------------------- Carga robusta -----------------------------------------
with open(RUTA, "r", encoding="latin1") as f:
    sep = ";" if ";" in f.readline() else ","

df = pd.read_csv(RUTA, sep=sep, encoding="latin1")
df = normalizar_dataset(df)
if "id_depatamento" in df.columns:
    df = df.rename(columns={"id_depatamento": "id_departamento"})

print("\n--- Caracterización de Datos ---")
print("Filas, Columnas:", df.shape)
print(df.isnull().sum())

# --------------------- Filtro dinámico --------------------------------------
col_horas = "promedio_diario_en_horas"
if col_horas not in df.columns:
    raise KeyError("Columna promedio_diario_en_horas ausente")

# Filtro opcional por municipio
entrada = input("Ingrese ID de municipio (opcional, Enter para todos): ").strip()
df_sel = pd.DataFrame()
nombre_filtro = ""

if entrada:
    id_mun = int(entrada)
    df_sel = df[df["id_municipio"] == id_mun]
    if df_sel.empty:
        raise ValueError("Municipio no encontrado")
    nombre_filtro = df_sel["municipio"].iloc[0].replace("_", " ").title()
else:
    df_sel = df
    nombre_filtro = "Todos los municipios"

# Descripción del análisis
descripcion = input("Descripción breve del análisis (opcional): ").strip()

# Filtrar horas válidas
mask = (df_sel[col_horas] > 0) & (df_sel[col_horas] <= 24)
df_fil = df_sel[mask]

# --------------------- Estadísticas -----------------------------------------
print("\n========================================================")
if descripcion:
    print(f"🔎 Análisis: {descripcion}")
print(f"--- Estadísticas para {nombre_filtro} ---")
print("========================================================")
mostrar_promedio(df_fil, col_horas)
mostrar_mediana(df_fil, col_horas)
mostrar_varianza(df_fil, col_horas)
mostrar_desviacion_estandar(df_fil, col_horas)
mostrar_percentiles(df_fil, col_horas)
posicion_percentil(df_fil, col_horas, 5)

# --------------------- Gráficas ---------------------------------------------

graficar_distribucion_normal(df_fil, col_horas)
graficar_promedio(df_fil, col_horas)
graficar_boxplot(df_fil, col_horas)
graficar_histograma(df_fil, col_horas)
graficar_barras_categoria(df_fil, col_horas)

vars_num = [v for v in ["energia_activa", "energia_reactiva", "potencia_maxima", col_horas] if v in df_fil.columns]
if len(vars_num) >= 2:
    graficar_matriz_correlacion(df_fil, vars_num)
    if {"potencia_maxima", col_horas}.issubset(df_fil.columns):
        graficar_dispersion(df_fil, "potencia_maxima", col_horas)
    if {col_horas, "energia_activa"}.issubset(df_fil.columns):
        graficar_regresion_lineal(df_fil, col_horas, "energia_activa")
else:
    print("⚠️  Insuficientes variables numéricas para correlación/regresión")
