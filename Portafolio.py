#frond-end - Lara Berenice Ledesma

import streamlit as st
import base64
import urllib.parse
import requests
from urllib.parse import quote
from datetime import datetime
import os
import re

# Configuración de la página
st.set_page_config(page_title="Servicios de Consultoría en Gestión Ambiental y Desarrollo Sostenible", layout="wide")

# Estilos personalizados
st.markdown("""
<style>
/* Estilo general para escritorio */
.titulo-contenedor {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-top: 5px;
    margin-bottom: 0;
}

div.tarjeta {
    background-color:rgba(204, 232, 198, 0.6);
    padding: 25px;
    margin-top: 20px;
    border-radius: 18px;
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
}

.img-servicio {
    width: 100%;
    height: 160px;
    overflow: hidden;
    border-radius: 12px;
    margin-bottom: 8px;
}

.img-servicio img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}


.tarjeta {
    height: 100%;
    min-height: 260px;
    display: flex;
    flex-direction: column;
    padding: 20px;

}

.header-container {
    display: flex;
    align-items: center;
    justify-content: flex-start;  /* ← izquierda */
    gap: 15px; /* mejor que margin-right */
    width: 100%;
    margin-left: 0;
}

.logo {
    width: 150px;
    height: 170px;
    object-fit: contain;
    border-radius: 20px;
    margin-right: 0px; /* separación normal */
}

.titulo-texto {
    max-width: 950px;
}

.titulo-texto h3 {
    font-size: 40px;
    text-align: left;   /* ← izquierda */
    margin: 0;
    font-weight: bold;
}


/* Responsive para móvil */
@media (max-width: 768px) {
    .titulo-contenedor {
        flex-direction: column !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 0 !important;
        padding: 0 !important;
        text-align: center;
        gap: 10px;
    }

    .logo {
        width: 120px !important;
        height: auto !important;
        margin: 0 0 10px 32px !important; /* top, right, bottom, left */
    }
    
    .titulo-texto {
        text-align: left !important;
        margin-left: 20px !important;
        margin-right: 10px !important;
    }

    .titulo-texto h3 {
         font-size: 22px !important;
        text-align: left !important;   /* ← clave */
        margin-left: 20px !important;  /* ajustá este valor */
        margin-right: 10px !important;
        
    }

    /* Botones en columna */ 
    .css-1lcbmhc.e1fqkh3o3 {
        flex-direction: column !important;
        align-items: center !important;
    }

    .stButton > button {
        font-size: 18px !important;
        padding: 10px 14px !important;
        min-width: 60px !important;
        margin: 5px !important;
        border-radius: 8px !important;
        width: auto !important;
    }

    #modo-switch {
        text-align: right !important;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    
}
</style>
""", unsafe_allow_html=True)


# Script para detectar móvil
st.markdown("""
    <script>
    const mediaQuery = window.matchMedia('(max-width: 768px)');
    if (mediaQuery.matches) {
        window.parent.postMessage({ type: 'streamlit:setComponentValue', key: 'mobile', value: true }, '*');
    } else {
        window.parent.postMessage({ type: 'streamlit:setComponentValue', key: 'mobile', value: false }, '*');
    }
    </script>
""", unsafe_allow_html=True)

if 'mobile' not in st.session_state:
    st.session_state.mobile = False  # fallback

# Función para imagen en base64
def imagen_base64(ruta):
    with open(ruta, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64}"

# Inicialización del modo
if 'mode' not in st.session_state:
    st.session_state.mode = "Modo Día"

# Línea superior con logo + descripción + botones
top_col1, top_col2 = st.columns([6, 1])

with top_col1:
    logo = imagen_base64("Imagenes/b_blanco.png")
    
    
    st.markdown(f"""
    <div class="header-container">
        <img src="{logo}" class="logo">
        <div class="titulo-texto">
            <h3>Servicios de Consultoría en Gestión Ambiental y Desarrollo Sostenible</h3>
            <p>
                ESG, cumplimiento normativo ambiental, gestión de riesgos ambientales,
                regulatorios y optimización del desempeño ambiental en proyectos e industrias.
            </p>
        </div>
    </div>
    """.format(logo), unsafe_allow_html=True)
    
    
    
    

    
    with top_col2:
    # Encapsular los botones en un div con ID para CSS específico
        st.markdown('<div id="modo-switch">', unsafe_allow_html=True)
        col_sol, col_luna = st.columns(2)
        with col_sol:
            if st.button("☀️"):
                st.session_state.mode = "Modo Día"
        with col_luna:
            if st.button("🌙"):
                st.session_state.mode = "Modo Noche"
        st.markdown('</div>', unsafe_allow_html=True)

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
            <div class="tarjeta" style='padding: 10px; border-radius: 10px;'
            style="list-style-type: disc; padding-left: 30px;">
            
    <li><strong>Estudios de Impacto Ambiental (EIA)</strong>
        <p>Evaluación de impactos y viabilidad ambiental de proyectos productivos,
        energéticos, mineros y de infraestructura.</p>
    </li>

    <li><strong>Planes de Gestión Ambiental (PGA)</strong>
        <p>Diseño de planes integrales con enfoque en desarrollo sostenible,
        mejora continua y responsabilidad social.</p>
    </li>

    <li><strong>Auditorías Ambientales</strong>
        <p>Auditorías de cumplimiento normativo y detección de riesgos ambientales.</p>
    </li>

    <li><strong>Evaluación Socioambiental y Económica</strong>
        <p>Análisis integral de proyectos con herramientas de valoración ambiental.</p>
    </li>

    <li><strong>Residuos, Efluentes y Energía</strong>
        <p>Planes técnicos con enfoque en economía circular.</p>
    </li>

    <li><strong>Datos Ambientales y Reportes ESG</strong>
        <p>Dashboards e indicadores para reportes ambientales y de sostenibilidad.</p>
    </li>

    <li><strong>Monitoreo Ambiental</strong>
        <p>Toma de muestras y análisis técnico ambiental.</p>
    </li>

    <li><strong>Componente Social y ESG</strong>
        <p>Integración de criterios sociales y sostenibles en proyectos.</p>
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
        