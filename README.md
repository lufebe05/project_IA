# Proyecto IA: Sistema de Mantenimiento Predictivo (AI4I 2020 - UCI Machine Learning Repository)
http://archive.ics.uci.edu › datasets

Proyecto para la Especialización en Ciencia de Datos e Inteligencia Artificial (Universidad de Medellín). El objetivo es predecir fallas en maquinaria industrial utilizando técnicas de Machine Learning para optimizar procesos de mantenimiento y reducir costos por paradas no programadas.

---

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.14.4 (Gestionado con `uv`)
* **Entorno:** Windows 11
* **Editor/IDE:** VScode
* **Terminal:** Powershell
* **Control de Versiones:** Git & GitHub (SSH)
* **Stack IA:** Scikit-learn, Imbalanced-learn (Oversampling), Pandas, NumPy.
* **Visualización:** Seaborn & Matplotlib.

---

## 📊 Pipeline del Proyecto
El proyecto ha completado las siguientes fases críticas:

1.  **EDA:** Análisis exploratorio identificando un fuerte desbalance de clases (96.6% normal vs 3.4% falla).
2.  **Preprocesamiento:** * Eliminación de redundancias (Air temperature) y fuga de datos (causas específicas de falla).
    * Balanceo de datos mediante **RandomOverSampler** para mejorar la detección de minorías.
3.  **Evaluación de Modelos:** Creación de una clase personalizada para pruebas automatizadas (`ModelEvaluation`).
4.  **Modelo Ganador:** Implementación de **Random Forest**, logrando un balance óptimo entre precisión y estabilidad.

---

## 🏆 Resultados del Modelo (Random Forest)
Tras comparar múltiples algoritmos, el Bosque Aleatorio obtuvo los mejores resultados:

* **Accuracy:** 99.46%
* **Cross Validation (Estabilidad):** 96.38%
* **Fallas Detectadas (Recall):** 100% (Cero falsos negativos)
* **AUC Score:** 0.99

---

## 📂 Estructura del Proyecto
* `data/`: Datasets originales y procesados.
* `notebooks/`: Experimentación con Regresión Logística, KNN, Árboles de Decisión y Random Forest.
* `models/`: Archivos `.joblib` con los modelos entrenados listos para producción.
* `src/`: Scripts de procesamiento y lógica de predicción.

---

## 🚀 Configuración del Entorno Local

1. **Clonar el repositorio:**
   ```bash
   git clone git@github.com:lufebe05/project_IA.git
   cd project_IA