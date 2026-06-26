import streamlit as st
import math

# Configuración de la página
st.set_page_config(page_title="Calculador de Racks - CEDIS", page_icon="🛞", layout="centered")

st.title("🛞 Calculador de Espacio y Racks para Llantas")
st.write("Calcula cuántos cubos/racks necesitas según las medidas ISO de la llanta y las reglas de desborde de tu almacén.")

st.sidebar.header("1. Dimensiones del Rack Estándar")
rack_largo = st.sidebar.number_input("Largo del rack (cm)", value=122.0)
rack_ancho = st.sidebar.number_input("Ancho del rack (cm)", value=122.0)
rack_alto = st.sidebar.number_input("Alto del rack (cm)", value=152.0)

st.header("2. Datos de la Llanta")
col1, col2, col3 = st.columns(3)

with col1:
    ancho_mm = st.number_input("Ancho (Ej: 175)", value=175, step=5)
with col2:
    perfil = st.number_input("Perfil / Relación (Ej: 65)", value=65, step=5)
with col3:
    rin_pulg = st.number_input("Rin en pulgadas (Ej: 14)", value=14, step=1)

st.header("3. Parámetros de Almacenamiento")
total_llantas_objetivo = st.number_input("Cantidad total de llantas a almacenar", value=500, step=50)

# Regla de desborde basada en nuestra conversación
regla_desborde = st.selectbox(
    "Límite de desborde permitido hacia los lados",
    ["Sin desborde (Estricto)", "Máximo 1/4 de la llanta", "Máximo 1/2 de la llanta (Punto de equilibrio)", "Forzar 6 pilas (Configuración de 54 llantas)"]
)

# --- CÁLCULOS MATEMÁTICOS ISO ---
# Conversiones básicas
ancho_cm = ancho_mm / 10.0
rin_cm = rin_pulg * 2.54
flanco_cm = (ancho_mm * (perfil / 100.0)) / 10.0
diametro_total = rin_cm + (2 * flanco_cm)

# Factor de compactación por peso (reducción del ancho nominal al estar acostadas)
factor_compactacion = 0.93  # Reduce aprox un 7% el grosor
altura_efectiva_llanta = ancho_cm * factor_compactacion

# --- LÓGICA DE PILAS SEGÚN DESBORDE ---
llantas_por_pila = math.floor(rack_alto / altura_efectiva_llanta)

# Forzar ajustes específicos basados en la realidad operativa del CEDIS
if regla_desborde == "Sin desborde (Estricto)":
    columnas_base = math.floor(rack_largo / diametro_total) * math.floor(rack_ancho / diametro_total)
    if columnas_base == 0: columnas_base = 1 # Al menos entra una

elif regla_desborde == "Máximo 1/4 de la llanta":
    # Si la medida es la 175/65R14 o similar, entran 5 por distribución cruzada
    if diametro_total <= 60.0:
        columnas_base = 5
    else:
        columnas_base = 4 # Para llantas más grandes como la 185

elif regla_desborde == "Máximo 1/2 de la llanta (Punto de equilibrio)":
    if diametro_total <= 60.0:
        columnas_base = 9  # Distribución extrema de 3x3
    else:
        columnas_base = 5  # Distribución cruzada para medianas

elif regla_desborde == "Forzar 6 pilas (Configuración de 54 llantas)":
    columnas_base = 6
    llantas_por_pila = 9 # Forzamos la altura recomendada y segura

# Capacidad total por cada rack individual
capacidad_por_rack = columnas_base * llantas_por_pila

# Calcular cantidad de racks necesarios
if capacidad_por_rack > 0:
    racks_necesarios = math.ceil(total_llantas_objetivo / capacidad_por_rack)
else:
    racks_necesarios = 0

# --- PRESENTACIÓN DE RESULTADOS ---
st.markdown("---")
st.subheader("📊 Resultados del Análisis")

metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
with metrics_col1:
    st.metric("Diámetro de Llanta", f"{diametro_total:.2f} cm")
with metrics_col2:
    st.metric("Llantas por Rack", f"{capacidad_por_rack} pzas")
with metrics_col3:
    st.metric("Pilas por Rack", f"{columnas_base} columnas de {llantas_por_pila} de alto")

st.markdown(f"### 🚚 Cubos / Racks totales requeridos: **{racks_necesarios}**")

st.info(f"""
**Ficha Técnica del Acomodo:**
* **Grosor estimado de llanta bajo estiba (compactada):** {altura_efectiva_llanta:.2f} cm (Ancho original: {ancho_cm} cm).
* Cada columna o pila ocupará verticalmente unos **{llantas_por_pila * altura_efectiva_llanta:.1f} cm** de los {rack_alto} cm disponibles en el rack.
""")