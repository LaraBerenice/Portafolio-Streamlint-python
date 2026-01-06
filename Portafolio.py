
#frond-end - Lara Berenice Ledesma

import streamlit as st
import base64
import urllib.parse
import requests
from urllib.parse import quote
from datetime import datetime
import os
import re

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(
    page_title="Servicios de Consultoría en Gestión Ambiental y Desarrollo Sostenible",
    layout="wide"
)

# =========================
# ESTADO DEL MODO
# =========================
if "mode" not in st.session_state:
    st.session_state.mode = "Modo Día"

# =========================
# FUNCIÓN IMÁGENES
# =========================
def imagen_base64(ruta):
    with open(ruta, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

# =========================
# CSS GLOBAL + POSICIONAMIENTO REAL
# =========================
st.markdown("""
<style>

* ===== BOTONES IZQUIERDA FIJA ===== */
div.stButton {
    width: auto !important;
    display: flex !important;
    justify-content: flex-start !important;
    margin-top: 1px;
}

div.stButton > button[aria-label="day"],
div.stButton > button[aria-label="night"] {
    position: fixed !important;
    top: 20px !important;
    z-index: 10001 !important;
    padding: 6px 12px !important;
    font-size: 16px !important;
    font-weight: bold !important;
    border-radius: 6px !important;
}

div.stButton > button[aria-label="day"] {
    left: 20px !important;
}

div.stButton > button[aria-label="night"] {
    left: 70px !important;
}

/* Texto modo */
.modo-texto {
    position: fixed !important;
    top: 60px !important;
    left: 20px !important;
    font-weight: bold !important;
    font-size: 16px !important;
    z-index: 10001 !important;
}

/* ===== HEADER VERTICAL ===== */
.header-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 10px;
    margin-top: 40px;
}

.logo {
    width: 150px;
    height: 150px;
    object-fit: contain;
    border-radius: 15px;
    margin-top: -170px;
}

.titulo-texto h3 {
    font-size: 40px;
    margin: 0;
}

/* ===== SUBTÍTULO ===== */
.texto-descripcion {
    background-color: #4CAF50;
    color: white;
    padding: 8px 20px;
    margin-top: 10px;
    border-radius: 10px;
    font-size: 18px;
    line-height: 1.5;
    font-weight: 500;
    max-width: 900px;
}

/* ===== TARJETAS ===== */
.tarjeta {
    background-color: rgba(204, 232, 198, 0.6);
    padding: 25px;
    border-radius: 18px;
}

/* ===== MOBILE ===== */
@media (max-width: 768px) {
    div.stButton > button[aria-label="day"] {
        top: 10px !important;
        right: 60px !important;
        font-size: 14px !important;
    }

    div.stButton > button[aria-label="night"] {
        top: 10px !important;
        right: 10px !important;
        font-size: 14px !important;
    }

    .modo-texto {
        top: 45px !important;
        right: 10px !important;
        font-size: 14px !important;
    }

    .logo {
        width: 100px;
        margin-top: -170px;
    }

    .titulo-texto h3 {
        font-size: 22px;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# BOTONES (SIN CONTENEDORES HTML)
# =========================
if st.button("☀️", key="day"):
    st.session_state.mode = "Modo Día"

if st.button("🌙", key="night"):
    st.session_state.mode = "Modo Noche"

# =========================
# LÓGICA DE CAMBIO DE MODO
# =========================
query_params = st.query_params  # <-- reemplazo actualizado
if "mode" in query_params:
    if query_params["mode"][0] == "day":
        st.session_state.mode = "Modo Día"
    elif query_params["mode"][0] == "night":
        st.session_state.mode = "Modo Noche"


# Logo
logo = imagen_base64("Imagenes/b_blanco.png")

# Encabezado

st.markdown(f"""
<div class="header-container">
    <img src="{logo}" class="logo">
    <div class="titulo-texto">
        <h3>Servicios de Consultoría en Gestión Ambiental</h3>
    </div>
    <div class="texto-descripcion">
    Desarrollo Sostenible · Cumplimiento Normativo Ambiental · Gestión y Prevención de Riesgos Ambientales · EIA · PGA · SGA · ESG · Mejora Continua
    </div>
</div>
""", unsafe_allow_html=True)



# 🎨 Estilos por modo
if st.session_state.mode == "Modo Noche":
    fondo = imagen_base64("Imagenes/Campo nocturno bajo la luna llena.png")
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: #2E2E2E;
            color: #FFFFFF;
            background-image: url('{fondo}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader, .stCaption, .stCode {{
            color: #FFFFFF !important;
        }}
        .stButton>button {{
            background-color: #333333;
            color: #FFFFFF;
            border: 1px solid #FFFFFF;
            font-weight: bold !important;
        }}
        .stImage {{
            border: none !important;
        }}
        .profesora-info {{
            background-color: #7A9D6B;
            padding: 20px;
            color: #E8FFE8;
            border-radius: 20px;
            text-align: center;
            line-height: 1.8;
        }}
        input, textarea, label, .stCheckbox > div {{
            color: black !important;
        }}
        .stForm {{
            background-color: #7A9D6B !important;
            padding: 20px;
            border-radius: 10px;
        }}
        </style>
    """, unsafe_allow_html=True)
else:
    fondo = imagen_base64("Imagenes/Campo agrícola y paneles solares.png")
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: #A8D08D;
            color: #006400;
            background-image: url('{fondo}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader, .stCaption, .stCode {{
            color: #333333 !important;
        }}
        .stButton>button {{
            background-color: #4CAF50;
            color: white;
            border: 1px #4CAF50 solid;
            font-weight: bold !important;
            font-size: 15px !important;
        }}
        .stImage {{
            border: 2px solid #00000000;
        }}
        .profesora-info {{
            background-color: #4CAF50;
            padding: 20px;
            color: #2F4F2F;
            border-radius: 20px;
            text-align: center;
            line-height: 1.8;
        }}
        input, textarea, label, .stCheckbox > div {{
            color: black !important;
        }}
        .stForm {{
            background-color: #4CAF50 !important;
            padding: 20px;
            border-radius: 10px;
        }}
        </style>
    """, unsafe_allow_html=True)  


with st.container():
        col1, = st.columns(1)
        with col1:
            st.markdown(f"""            
            <div class="tarjeta"style="padding: 10px; border-radius: 10px; list-style-type: disc">
            
    <li><strong>Estudios de Impacto Ambiental (EIA)</strong>
        <p>Elaboración de Estudios de Impacto Ambiental para proyectos
        de agroindustria, minería, energía, construcción e industria,
        orientados a evaluar impactos, garantizar el cumplimiento normativo y
        asegurar la viabilidad ambiental de los proyectos.</p>
    </li>

    <li><strong>Planes Integrales de Gestión Ambiental (PGA)</strong>
        <p>Diseño de Planes de Gestión Ambiental integrales,
        incorporando criterios de desarrollo sostenible, mejora continua
        y desempeño ambiental, junto con aspectos de seguridad alimentaria,
        salud y seguridad laboral, responsabilidad social empresaria, calidad e inocuidad.</p>
    </li>

    <li><strong>Auditorías Ambientales y Cumplimiento Normativo</strong>
        <p>Ejecución de auditorías ambientales y legales para identificar desvíos,
        riesgos y oportunidades de mejora, fortaleciendo los sistemas de gestión
        y asegurando alineación con normativas vigentes, Buenas Prácticas Agrícolas (BPA),
        incorporando criterios de desarrollo sostenible, mejora continua, aspectos de seguridad
        alimentaria, salud y seguridad laboral, responsabilidad social empresaria,
        calidad e inocuidad y estándares ambientales aplicables.</p>
    </li>

    <li><strong>Evaluación Socioambiental, Económica y Financiera de Proyectos</strong>
        <p>Análisis integral de proyectos de inversión productivos, energéticos y
        de infraestructura, incorporando evaluación económica, financiera y herramientas
        de Valoración Económica Ambiental (VEA) para apoyar decisiones estratégicas
        sostenibles.</p>
    </li>

    <li><strong>Gestión de Residuos, Efluentes y Eficiencia Energética</strong>
        <p>Desarrollo de planes técnicos para la gestión de residuos, tratamiento
        de efluentes y mejora de la eficiencia energética, con enfoque en economía circular,
        optimización de recursos y reducción de impactos ambientales.</p>
    </li>

    <li><strong>Datos Ambientales y Reportes ESG</strong>
        <p>Análisis de datos ambientales y diseño de dashboards para el monitoreo de indicadores,
        utilizados como soporte para Reportes de Gestión Ambiental y Reportes de Sostenibilidad
        (ESG), facilitando la toma de decisiones basada en datos.</p>
    </li>
    
      <li><strong>Informes Técnicos y Periciales</strong>
        <p>Elaboración de informes técnicos y periciales de parte vinculados a la gestión
        ambiental o la valoración económica ambiental técnica de proyectos o industrias.</p>
    </li>

    <li><strong>Monitoreo Ambiental y Toma de Muestras</strong>
        <p>Realización de muestreos ambientales en entornos productivos, industriales
        o de obras, aplicando métodos analíticos y técnicas de campo para la detección
        y evaluación de contaminación ambiental.</p>
    </li>

    <li><strong>Integración del Componente Social y Enfoque ESG</strong>
        <p>Incorporación del componente social en proyectos y actividades, integrando
        criterios ESG y un enfoque de desarrollo sostenible, con el objetivo de fortalecer
        la aceptación social y el impacto positivo de los mismos.
        </p>
    </li>
    </div>
    """, unsafe_allow_html=True)


            
        
st.markdown("""
        <div style="padding: 0px; border-radius: 10px;">
        <h3 style="font-size: 28px;">📞 Contacto</h3>
        <div style='text-align: center; margin-top: 0px; background-color: rgba(220,220,220,0.8); padding: 15px; border-radius: 10px;'>
            <h3 style='color: #2E8B57;'>Reserva tu turno para consultas por video llamada:</h3>
            <!-- Botón Google Calendar -->
            <a href="https://calendar.app.google/FBMp55BPqbiwsfaP7" target="_blank">
                <button style='background-color: #4CAF50; color: white; font-weight: bold; font-size: 18px; padding: 10px 25px; border: none; border-radius: 8px; margin: 5px;'>
                    📅 Reservar turno
                </button>
            
            
        </div>
    """, unsafe_allow_html=True)


    

    # Correo electrónico
st.markdown(
            f'''
            <p>
            
            </p>
            
             <p>
            
            </p>
            
            <a href="mailto:berenice.ledesma12345@gmail.com">
                <button style="background-color: #4285F4; color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                    ✉️ Consultas por correo
                </button>
            </a>
            ''',
            unsafe_allow_html=True
        )


# 📲 Botón flotante de WhatsApp
st.markdown("""
            <a href='https://wa.me/+5493704003126' target='_blank'>
                <img src="https://img.lovepik.com/png/20231104/whatsapp-phone-icon-logo-whatsapp-digital-green_494222_wh860.png" alt="WhatsApp" width="60" height="60" style="position: fixed; bottom: 30px; right: 30px; border-radius: 50%; box-shadow: 0 0 10px rgba(0,0,0,0.2);"/>
            </a>
        """, unsafe_allow_html=True)
        