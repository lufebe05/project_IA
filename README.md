# Proyecto IA: Sistema de Mantenimiento Predictivo IA (AI4I 2020)

Proyecto para la especialización en Ciencia de Datos e Inteligencia Artificial. El objetivo es predecir fallas en maquinaria industrial utilizando el dataset AI4I 2020 y el modelo de lenguaje Gemma para la asistencia al usuario. 

---

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.14.4
* **Gestor de Entorno:** [uv](https://github.com/astral-sh/uv) (Gestión de paquetes ultrarrápida)
* **Editor:** Cursor (AI Code Editor)
* **Terminal:** PowerShell
* **Control de Versiones:** Git & GitHub (Conexión segura vía SSH)
* **Librerías Base:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn.
* **Dataset:** [AI4I 2020 Predictive Maintenance](https://www.kaggle.com/datasets/stephanmathew/predictive-maintenance-dataset-ai4i-2020)

---

## 📂 Estructura del Proyecto
El proyecto sigue una estructura profesional de Ciencia de Datos:

* `data/`: Almacenamiento de datasets (Raw para datos brutos y Processed para datos limpios).
* - `data/raw/`: Dataset original sin modificaciones.
* - `data/procesado/`: (Pendiente) Datos tras limpieza y feature engineering.
* `notebooks/`: Jupyter Notebooks para análisis exploratorio (EDA) y experimentación.
* `src/`: Scripts de Python (.py) para procesamiento y modelos finales.
* `pyproject.toml`: Archivo maestro de configuración de dependencias.
* `uv.lock`: Registro de versiones exactas para reproducibilidad.

---

### 📝 Notas de la Sesión Actual
1. Configuración del entorno con `uv`.
2. Instalación de: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `ipykernel`.
3. Creación del notebook `01_eda_mantenimiento.ipynb`.
4. Verificación de carga exitosa del DataFrame original.

---

## 🚀 Configuración del Entorno Local

Para replicar este entorno en tu máquina, sigue estos pasos:

1. **Clonar el repositorio:**
   ```powershell
   git clone git@github.com:lufebe05/project_IA.git
   cd project_IA