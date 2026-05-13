# Sistema de Mantenimiento Predictivo 🛠️
### Dataset: AI4I 2020 - UCI Machine Learning Repository
http://archive.ics.uci.edu › datasets

Este proyecto ha sido desarrollado como parte de la **Especialización en Ciencia de Datos e Inteligencia Artificial** de la **Escuela de Ingeniería de Antioquia (EIA)**. El objetivo principal es predecir fallas en maquinaria industrial mediante técnicas avanzadas de Machine Learning, optimizando los ciclos de mantenimiento y reduciendo costos operativos por paradas no programadas.

---

## 🛠️ Tecnologías y Stack Técnico

* **Lenguaje:** Python 3.12+ (Gestionado de forma eficiente con `uv`)
* **Editor & Terminal:** Cursor / VS Code + Warp
* **Control de Versiones:** Git & GitHub (SSH)
* **Stack de Datos:** Pandas, NumPy, Scikit-learn.
* **Balanceo de Datos:** Imbalanced-learn (RandomOverSampler).
* **Visualización:** Seaborn & Matplotlib.
* **Despliegue:** Streamlit.

---

## 📊 Pipeline del Proyecto

El desarrollo se estructuró en cuatro fases críticas para garantizar la robustez del modelo:

1.  **Análisis Exploratorio (EDA):** Identificación de un fuerte desbalance de clases (96.6% estado normal vs. 3.4% fallas).
2.  **Preprocesamiento Avanzado:** 
    * Eliminación de redundancias térmicas y variables que generaban *data leakage* (fuga de datos).
    * Aplicación de **RandomOverSampler** para equilibrar la representatividad de las fallas.
3.  **Evaluación de Modelos:** Implementación de una clase personalizada `ModelEvaluation` para automatizar pruebas comparativas.
4.  **Modelo Final:** **Random Forest**, seleccionado por su excepcional capacidad de generalización y estabilidad.

---

## 🏆 Resultados del Modelo (Random Forest)

El modelo final presenta métricas de alto rendimiento, ideales para entornos industriales donde omitir una falla es crítico:

| Métrica | Resultado |
| :--- | :--- |
| **Accuracy** | 99.46% |
| **Recall (Detección de Fallas)** | 100% |
| **Cross Validation** | 96.38% |
| **AUC Score** | 0.99 |

---

## 📂 Estructura del Repositorio

```text
├── data/               # Datasets originales y procesados
├── notebooks/          # Experimentación (LR, KNN, DT, Random Forest)
├── src/
│   ├── models/         # Modelos entrenados (.joblib)
│   └── processing/     # Scripts de lógica y preprocesamiento
├── app.py              # Aplicación de interfaz con Streamlit
└── pyproject.toml      # Configuración del entorno con uv
---

## 🚀 Configuración del Entorno Local

1. **Clonar el repositorio:**
   ```bash
   git clone git@github.com:lufebe05/Lu-clasificacion-maquinaria
   cd Lu-clasificacion-maquinaria

2. **Ejecucion de la app en Streamlit**
    ```bash
    uv run streamlit run app.py
    **En caso de requerir una instalación de dependencias en tiempo de ejecución, utiliza:**
    uv run --with streamlit streamlit run app.py

Desarrollado por: Luis Fernando Betancurt Betancourt
Institución: Universidad de Medellin (UdeM)