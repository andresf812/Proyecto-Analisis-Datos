# Proyecto de Análisis de Datos - Consumo Energético por Municipio

Este proyecto realiza un análisis exploratorio del consumo energético en distintos municipios de Colombia, utilizando datos proporcionados en formato CSV. A través de la limpieza de datos, generación de estadísticas y visualizaciones gráficas, se identifican patrones y se resaltan municipios con comportamientos críticos o destacados.

---

## 📊 Objetivos

- Limpiar y transformar datos crudos sobre consumo energético.
- Calcular estadísticas descriptivas clave (promedios, máximos, desviaciones, percentiles).
- Generar visualizaciones para facilitar la interpretación de resultados.
- Identificar municipios con consumo crítico o anómalo.

---

## 🗂️ Estructura del Proyecto  

```bash
Proyecto-Analisis-Datos/
├── data/
│   ├── Zonas.csv                  # Datos originales
│   └── Zonas_limpio.csv           # Datos limpios
├── scripts/
│   ├── limpieza.py                # Funciones de limpieza de datos
│   ├── limpiar_y_guardar.py       # Script para limpiar y guardar CSV
│   ├── estadisticas.py            # Funciones estadísticas descriptivas
│   ├── graficas.py                # Funciones para visualizaciones
│   └── main.py                    # Script principal de ejecución
├── images/
│   ├── boxplot_promedio_diario_en_horas_por_municipio.png
│   └── dispersion_energia_activa_vs_promedio_diario_en_horas.png
├── requirements.txt
├── README.md
└── LICENSE
