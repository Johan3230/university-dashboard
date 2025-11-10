import streamlit as st
import pandas as pd

# --- Load Dataset ---
@st.cache_data
def load_data():
    df = pd.read_csv("university_student_data.csv")
    return df

df = load_data()

st.title("🎓 Panel de datos de estudiantes universitarios ")
st.write("Analiza retención, satisfacción y matriculas por año y periodo académico.")

# --- Sidebar Filters ---
years = st.sidebar.multiselect("Selecciona Año(s)", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
terms = st.sidebar.multiselect("Selecciona Term(s)", sorted(df["Term"].unique()), default=sorted(df["Term"].unique()))

df_filtered = df[(df["Year"].isin(years)) & (df["Term"].isin(terms))]

# --- KPI Metrics ---
col1, col2, col3 = st.columns(3)

col1.metric("Promedio Retención (%)", round(df_filtered["Retention Rate (%)"].mean(), 2))
col2.metric("Promedio Satisfacción (%)", round(df_filtered["Student Satisfaction (%)"].mean(), 2))
col3.metric("Total Estudiantes Matriculados", int(df_filtered["Enrolled"].sum()))

# --- Retention Trend ---
st.subheader("📈 Panel de datos de estudiantes universitarios")
retention_trend = df_filtered.groupby("Year")["Retention Rate (%)"].mean()
st.line_chart(retention_trend)

# --- Satisfaction by Year ---
st.subheader("😊 Satisfacción de los estudiantes por año")
satisfaction = df_filtered.groupby("Year")["Student Satisfaction (%)"].mean()
st.bar_chart(satisfaction)

# --- Comparison by Term ---
st.subheader("🏫 Comparación de inscripciones (Primavera vs Otoño)")
enrollment_term = df_filtered.groupby("Term")["Enrolled"].sum()
st.bar_chart(enrollment_term)

st.write("---")
st.write("Dashboard desarrollado con Streamlit • Datos institucionales simulados.")
