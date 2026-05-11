import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os

# ---------------------------------------------------------------------------
# Configuración de la página
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Mantenimiento Predictivo",
    page_icon="⚙️",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Carga del modelo con caché
# ---------------------------------------------------------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "notebooks", "modelo_mantenimiento_predictivo.joblib")

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)

model = load_model()

# ---------------------------------------------------------------------------
# Encabezado principal
# ---------------------------------------------------------------------------
st.title("⚙️ Sistema de Mantenimiento Predictivo")
st.subheader("Dataset AI4I 2020 · UCI Machine Learning Repository")
st.markdown(
    """
    Esta aplicación utiliza un modelo de **Random Forest** entrenado con datos reales de
    sensores industriales para predecir si una máquina está en riesgo de fallo.
    Ajusta los parámetros del sensor en el panel izquierdo y presiona el botón para
    obtener el diagnóstico en tiempo real.
    """
)

if model is None:
    st.error(
        f"No se encontró el archivo del modelo en `{MODEL_PATH}`. "
        "Asegúrate de que el archivo `.joblib` está en la carpeta `notebooks/`."
    )
    st.stop()

st.divider()

# ---------------------------------------------------------------------------
# Sidebar — parámetros de entrada
# ---------------------------------------------------------------------------
st.sidebar.header("🔧 Parámetros del Sensor")
st.sidebar.markdown("Ajusta los valores según la lectura actual de la máquina.")

# Type: LabelEncoder orden alfabético → H=0, L=1, M=2
type_label = st.sidebar.selectbox(
    "Tipo de máquina (Type)",
    options=["L — Baja calidad", "M — Calidad media", "H — Alta calidad"],
    index=0,
)
type_map = {"L — Baja calidad": 1, "M — Calidad media": 2, "H — Alta calidad": 0}
type_encoded = type_map[type_label]

process_temp = st.sidebar.slider(
    "Temperatura del proceso [K]",
    min_value=305.0,
    max_value=314.0,
    value=310.0,
    step=0.1,
    help="Rango real del dataset: 305.7 K – 313.8 K",
)

rotational_speed = st.sidebar.slider(
    "Velocidad de rotación [rpm]",
    min_value=1168,
    max_value=2886,
    value=1538,
    step=1,
    help="Rango real del dataset: 1168 – 2886 rpm",
)

torque = st.sidebar.slider(
    "Torque [Nm]",
    min_value=3.8,
    max_value=76.6,
    value=40.0,
    step=0.1,
    help="Rango real del dataset: 3.8 – 76.6 Nm",
)

tool_wear = st.sidebar.slider(
    "Desgaste de herramienta [min]",
    min_value=0,
    max_value=253,
    value=108,
    step=1,
    help="Rango real del dataset: 0 – 253 min",
)

# ---------------------------------------------------------------------------
# Panel de resumen de valores actuales
# ---------------------------------------------------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📊 Valores actuales del sensor")
    summary = pd.DataFrame(
        {
            "Parámetro": [
                "Tipo de máquina",
                "Temperatura del proceso [K]",
                "Velocidad de rotación [rpm]",
                "Torque [Nm]",
                "Desgaste de herramienta [min]",
            ],
            "Valor": [
                type_label.split("—")[0].strip(),
                f"{process_temp:.1f}",
                f"{rotational_speed}",
                f"{torque:.1f}",
                f"{tool_wear}",
            ],
        }
    )
    st.dataframe(summary, use_container_width=True, hide_index=True)

# ---------------------------------------------------------------------------
# Predicción
# ---------------------------------------------------------------------------
with col2:
    st.markdown("### 🤖 Diagnóstico de la máquina")

    # Orden exacto de columnas con el que fue entrenado el modelo:
    # Type | Process temperature [K] | Rotational speed [rpm] | Torque [Nm] | Tool wear [min]
    input_data = np.array([[type_encoded, process_temp, rotational_speed, torque, tool_wear]])

    if st.button("🔍 Predecir Estado de la Máquina", use_container_width=True):
        try:
            prediction = model.predict(input_data)[0]
            proba = model.predict_proba(input_data)[0]

            st.markdown("---")
            if prediction == 0:
                st.success("## ✅ Máquina en buen estado")
                st.markdown(
                    f"El modelo **no detecta riesgo de falla**. "
                    f"La probabilidad estimada de fallo es **{proba[1]*100:.1f}%**."
                )
            else:
                st.error("## 🚨 ¡Riesgo de Falla Detectado!")
                st.markdown(
                    f"El modelo **predice una falla inminente**. "
                    f"La probabilidad estimada de fallo es **{proba[1]*100:.1f}%**. "
                    "Se recomienda programar una revisión de inmediato."
                )

            st.markdown("**Probabilidad de fallo:**")
            st.progress(float(proba[1]))

        except Exception as exc:
            st.error(f"Error al realizar la predicción: {exc}")
    else:
        st.info("Ajusta los parámetros en el panel izquierdo y presiona el botón para obtener el diagnóstico.")

# ---------------------------------------------------------------------------
# Pie de página informativo
# ---------------------------------------------------------------------------
st.divider()
st.markdown(
    """
    <small>
    **Modelo:** Random Forest Classifier · Precisión en prueba: 99.4% · AUC: 0.99<br>
    **Dataset:** AI4I 2020 Predictive Maintenance Dataset — UCI Machine Learning Repository<br>
    **Nota:** <code>Air temperature [K]</code> fue excluida del modelo durante el EDA por alta colinealidad con
    la temperatura del proceso (r = 0.88).
    </small>
    """,
    unsafe_allow_html=True,
)
