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
st.set_page_config(page_title="Análisis de Datos, Agronegocios y Gestión Ambiental", layout="wide")

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

.logo {
    width: 155px;
    height: 155px;
    object-fit: contain;
    border-radius: 15px;
    margin-right: -35px;
    margin-top: 5px;
}

.titulo-texto h3 {
    font-size: 40px;
    text-align: center;
    margin-right: -100px;
    margin-top: 5px;
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
    }

    .logo {
        width: 100px !important;
        height: 100px !important;
        margin: 0 0 10px 32px !important; /* top, right, bottom, left */
    }

    .titulo-texto h3 {
        font-size: 22px !important;
        text-align: center !important;
        margin: 0 auto 0 32px !important; /* top, right, bottom, left */  
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
    logo = imagen_base64("Imagenes/logo.png")
    
    
    st.markdown(
    f"""
    <div class="titulo-contenedor">
        <img src="{logo}" class="logo">
        <div class="titulo-texto">
            <h3>
                Consultora Agroambiental 📊 🌱
            </h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    
    
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


# Columnas para navegación centrada
# Crear espacio en blanco a los costados para centrar los botones
espacio_izquierda, nav1, nav2, nav3, nav4, nav5, espacio_derecha = st.columns([2.2, 0.7, 0.72, 0.59,0.7,0.7, 2.2])

with nav1:
    if st.button("Servicios"):
        st.session_state.seccion = "Servicios"
           
with nav2:
    if st.button("Proyectos"):
        st.session_state.seccion = "Proyectos"
        
with nav3:
    if st.button("Cursos"):
        st.session_state.seccion = "Cursos"
        
with nav4:
    if st.button("Contacto"):
        st.session_state.seccion = "Contacto"

with nav5:
    if st.button("Blog"):
        st.session_state.seccion = "Blog"    

        
# Inicializar sección si no está definida
if 'seccion' not in st.session_state:
    st.session_state.seccion = "Servicios"

# CONTENIDO DE CADA SECCIÓN
if st.session_state.seccion == "Servicios":
    st.markdown("### 💼 Servicios")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        Servicio_1 = imagen_base64("Imagenes/Servicios/planNegocio.jpeg")
        st.image(Servicio_1, use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
            <h4>Plan de Negocio</h4>
            <p>Documento fundamental para organizar, estructurar y comunicar una idea de negocio. Contiene el análisis del entorno, definición de objetivos, estructura organizativa, estrategias operativas, y puede incorporar el plan de marketing, evaluación de inversiones y análisis de costos. Es ideal para presentar ante socios, inversores o instituciones de financiamiento.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        Servicio_2 = imagen_base64("Imagenes/Servicios/marketing-plan.jpg")
        st.image(Servicio_2, use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
            <h4>Plan de Marketing</h4>
            <p>Puede integrarse al plan de negocios o desarrollarse de manera independiente. Define las estrategias para posicionar productos o servicios en el mercado, identificando al público objetivo, canales de comunicación y acciones promocionales.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        Servicio_3 = imagen_base64("Imagenes/Servicios/Proyectos_de_Inversion.jpg")
        st.image(Servicio_3, use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
            <h4>Evaluación de Proyectos de Inversión</h4>
            <p>Análisis financiero que permite estimar la viabilidad y rentabilidad de un proyecto. Puede formar parte del plan de negocios o utilizarse como documento técnico específico para decisiones de inversión.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        Servicio_4 = imagen_base64("Imagenes/Servicios/costos.jpeg")
        st.image(Servicio_4, use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
            <h4>Análisis de Costos</h4>
            <p>Estudio detallado de la estructura de costos de una empresa o proyecto. Permite identificar márgenes, optimizar recursos y calcular precios de venta.</p>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        Servicio_5 = imagen_base64("Imagenes/Servicios/Dash.jpg")
        st.image(Servicio_5, use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
            <h4> Análisis y Dashboards descriptivos para Control de Gestión</h4>
            <p>Complemento visual y dinámico para todos los documentos anteriores. Desarrollo tableros interactivos que permiten monitorear indicadores clave (KPI), visualizar tendencias y facilitar la toma de decisiones.</p>
        </div>
        """, unsafe_allow_html=True)
        
        
#----- call to action ----
    
    
        # Llamada a la acción (CTA) al final de Servicios
    st.markdown("""
    <div style='text-align: center; margin-top: 30px; background-color: rgba(220,220,220,0.8); padding: 15px; border-radius: 10px;'>
        <h3 style='color: #2E8B57;'>¿Querés llevar tu proyecto al siguiente nivel?</h3>
        <p>Contame tu idea y te ayudo a convertirla en realidad.</p>
        <a href="https://wa.me/5493704003126?text=Hola,%20quiero%20hablar%20sobre%20los%20servicios%20que%20ofreces." target="_blank">
            <button style='background-color: #25D366; color: white; font-weight: bold; font-size: 18px; padding: 10px 25px; border: none; border-radius: 8px;'>📲 Pedime presupuesto por WhatsApp</button>
        </a>
    </div>
    """, unsafe_allow_html=True)

        
#-----------
# SECCIÓN PROYECTOS

elif st.session_state.seccion == "Proyectos":    
    st.markdown("### 🚀 Proyectos")
    col6, col7, col8, col9, col10, col11 = st.columns(6)
    
    with col6:
        Proyecto1 = imagen_base64("Imagenes/Proyectos/Brindis real.jpg")
        st.image(Proyecto1, use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
            <h4>Análisis de Inventarios</h4>
            <p>Fue un trabajo grupal cuyo objetivo fue analizar los inventarios de Brindis
            Real, una empresa dedicada a la comercialización de bebidas alcohólicas.
            Como parte del proyecto, desarrollamos un dashboard de control de gestión
            para optimizar los ingresos y egresos de stock en el almacén.</p>
            <a href="https://github.com/LaraBerenice/Analisis_de_Inventarios" style="color: #003366; font-weight: bold;">
            Ver más ... </a>
        </div>
        """, unsafe_allow_html=True)

    with col7:
        Proyecto2 = imagen_base64("Imagenes/Proyectos/MGV.png")
        st.image(Proyecto2, use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
            <h4>Análisis del Movimiento del Ganado Bovino en 2018 en Argentina</h4>
            <p>El proyecto tuvo como objetivo, en su etapa de training, analizar
            los ingresos y egresos de ganado bovino según el tipo de agronegocio
            y la zona geográfica, con el fin de facilitar la toma de decisiones
            en el sector ganadero. </p>
            <a href="https://github.com/LaraBerenice/Analisis-Movimiento-Ganado-Vacuno-Argentina-2018" style="color: #003366; font-weight: bold;">
            Ver más ... </a>
        </div>
        """, unsafe_allow_html=True)

    with col8:
        Proyecto3 = imagen_base64("Imagenes/Proyectos/granos_retail.webp")
        st.image(Proyecto3, use_container_width=True)

        st.markdown("""
        <div style="background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;">
            <h4>Análisis de datos con hojas de cálculo:</h4>
            <p>Dos proyectos:</p>
            <ul>
                <li>Análisis de la evolución histórica de la producción de granos
                de Argentina desde 1981 a 2020 en Excel, abarcando una amplia
                variedad de cultivos por tonelada y superficie producida.</li>
                <li>Análisis de ventas y costos en una tienda de retail en Google Sheets,
                con el objetivo de evaluar la rentabilidad, detectar oportunidades
                de mejora y optimizar la gestión comercial.</li>
            </ul>
            <a href="https://github.com/LaraBerenice/analisis-de-datos-en-excel-y-en-google-sheet" style="color: #003366; font-weight: bold;">
            Ver más … </a>
        </div>
        """, unsafe_allow_html=True)

   
    with col9:
        Proyecto4 = imagen_base64("Imagenes/Proyectos/awc.png")
        st.image(Proyecto4, use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
            <h4> Comercio electrónico internacional de bicicletas</h4>
            <p>Análisis de costos y ventas de un comercio electrónico de bicicletas
            a nivel internacional con la generacón de un dashboard en Power BI.</p>
            <a href="https://github.com/LaraBerenice/Adventure-Works-Cycles_-AWC-" style="color: #003366; font-weight: bold;">
            Ver más ... </a>

        </div>
        """, unsafe_allow_html=True)   
    with col10:
        Proyecto5 = imagen_base64("Imagenes/Proyectos/comidaRapida.png")
        st.image(Proyecto5, use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
            <h4>Negocio de Comida Rápida</h4>
            <p>El negocio buscaba organizar sus registros en una base de datos,
            las soluciones fueron creación de la base de datos, el modelado de la
            base de datos y la inserción de los datos.</p>
            <a href="https://github.com/LaraBerenice/Descubriendo_la_BD_Fast_Food" style="color: #003366; font-weight: bold;">
            Ver más ... </a>

        </div>
        """, unsafe_allow_html=True)
        
    with col11:
        Proyecto6 = imagen_base64("Imagenes/Proyectos/covid19.png")
        st.image(Proyecto6, use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
            <h4> Análisis de Mercado – Expansión del COVID-19 </h4>
            <p>Una empresa bioquímica solicitó un análisis sobre la expansión del
            COVID-19 en Latinoamérica, con el fin de tomar decisiones estratégicas
            para la comercialización de sus vacunas. ¿Dónde le conviene más invertir
            a Biogénesis? ¿En qué país?</p>
            <a href="https://github.com/LaraBerenice/Analisis_para_laboratorio_de_vacunacion_en_covid_19" style="color: #003366; font-weight: bold;">
            Ver más ... </a>

        </div>
        """, unsafe_allow_html=True) 
        

#---loque dicen los clientes ----       
            
    # Testimonios de clientes
    st.markdown("### 🗨️👥💬 Testimonios 🌟 ")
    st.markdown("""
    <div style="background-color: rgba(220, 220, 220, 0.6); padding: 15px; border-radius: 10px;">
        <p><strong>👩‍🌾 💬María G. (Productora agrícola):</strong> "El análisis de costos que me preparaste me ayudó a optimizar los gastos en la producción. ¡Gracias por tu dedicación!"</p>
        <p><strong>👨‍💼 💬 Pablo R. (Emprendedor):</strong> "Con tu plan de negocios pude conseguir el crédito que necesitaba. Excelente acompañamiento."</p>
        <p><strong>👩‍🔬 💬Laura M. (Ingeniera ambiental):</strong> "Tu diagnóstico fue clave para mejorar nuestros indicadores de impacto. ¡Gran profesionalismo y claridad técnica!"</p>
        <p><strong>👩‍💻 💬 Sofía T. (Analista de datos):</strong> "El dashboard que desarrollaste fue justo lo que necesitábamos para tomar decisiones más informadas. Muy recomendable."</p>
        <p><strong>👨‍🔧 💬 Andrés V. (Técnico agroindustrial):</strong> "El informe que elaboraste nos permitió detectar áreas de mejora en la cadena de producción. ¡Un trabajo impecable!"</p>
        <p><strong>👩‍🏫 💬 Clara S. (Docente universitaria):</strong> "Tu presentación sobre sostenibilidad fue muy clara y enriquecedora para mis alumnos. ¡Gracias por compartir tus conocimientos!"</p>
        <p><strong>👨‍💻 💬 Martín G. (Desarrollador de software):</strong> "La base de datos que estructuraste nos facilitó muchísimo el análisis de tendencias. Excelente trabajo técnico y compromiso."</p>
        <p><strong>👨‍💼 💬 Ricardo P. (Gerente comercial):</strong> "Gracias a tu análisis de mercado pudimos redirigir nuestras estrategias de venta de manera efectiva."</p>
        <p><strong>👨‍🌍 💬 Diego F. (Consultor en sostenibilidad):</strong> "Gracias a tu asesoramiento, pudimos diseñar una estrategia ambiental más efectiva para nuestros clientes."</p>
        <p><strong>👩‍💼 💬 Paula D. (Gerente de proyectos):</strong> "Tu enfoque estratégico y detallado fue fundamental para que lográramos nuestros objetivos de certificación ambiental."</p>
        <p><strong>👨‍🌾 💬 Esteban L. (Productor ganadero):</strong> "Tus recomendaciones sobre manejo sostenible marcaron una gran diferencia en nuestra productividad."</p>
        <p><strong>👩‍🔬 💬 Verónica M. (Especialista en calidad ambiental):</strong> "El informe técnico que entregaste superó nuestras expectativas en precisión y profundidad."</p>
        <p><strong>👩‍⚕️ 💬 Mariana R. (Coordinadora de programas de salud):</strong> "El estudio de impacto social que realizaste nos permitió fortalecer nuestras campañas de concientización."</p>
         <hr style="border: none; border-top: 2px solid #666; margin: 10px 0;">
        <p style="text-align: center; font-weight: bold; color: #444; font-size: 20px; margin: 10px;">Cada proyecto, un nuevo desafío superado. ¡Gracias por confiar! 💼✨</p>
        <p style="text-align: center; font-size: 26px; margin: 10px;">❤️</p>


</div>
    </div>
    """, unsafe_allow_html=True)

#------------------------

# SECCIÓN CURSOS

if st.session_state.seccion == "Cursos":
    
    modo_actual = "modo-noche" if st.session_state.mode == "Modo Noche" else "modo-dia"
    
    st.markdown("### 🎓 Cursos")
# Bloque principal con HTML y estilos personalizados

    html_content = """
<div class="profesora-info" style="color: #E0E0E0; font-family: Arial, sans-serif; line-height: 1.5;">
  <h2 style="color: #E8F5E9; margin-bottom: 25px; text-align: center;">
    🌿 Capacitaciones especializadas en ambiente, agro y herramientas transversales
  </h2>
  <hr style="border: 0; border-top: 2px solid #E0E0E0; margin: 15px 0;">
  <p><strong>📜  Marco Legal de los Certificados: </strong></p>
  <ul style="margin-left: 20px; list-style: none; padding-left: 0;">
    <li style="display: inline-flex; align-items: center; margin-bottom: 8px; color: #FFEB3B; font-size: 18px;">
      <span>⭐</span>
      <span style="color: #E0E0E0;">Ley 25.675 – Ley General del Ambiente</span>
    </li>
    <li style="display: inline-flex; align-items: center; margin-bottom: 8px; color: #FFEB3B; font-size: 18px;">
      <span>⭐</span>
      <span style="color: #E0E0E0;">Ley 27.592 – Ley Yolanda</span>
    </li>
    <li style="display: inline-flex; align-items: center; gap: 6px; margin-bottom: 8px; color: #FFEB3B; font-size: 18px;">
      <span>⭐</span>
      <span style="color: #E0E0E0;">Ley 27.621 – Ley de Educación Ambiental Integral</span>
    </li>
    <li style="display:  inline-flex; margin-bottom: 8px; color: #FFEB3B; font-size: 18px;">
      <span>⭐</span>
      <span style="color: #E0E0E0;"> Emitido por profesional reconocido por el
      Ministerio de Cultura y Educación de República Argentina y con MP en el Consejo
      de Profesionales Bioagroindustriales de la Repúbica Argentina.</span>
    </li>
  </ul>
  <hr style="border: 0; border-top: 2px solid #E0E0E0; margin: 15px 0;">


<ul style="color: #E0E0E0; font-family: Arial, sans-serif; line-height: 1.6; margin-top: 25px; padding-left: 0; text-align: left;">
  </li>
  <li style="display: inline-flex; align-items: center; gap: 6px; margin-bottom: 10px; font-size: 18px; color: #81C784;">
    <span>☄️ </span>
    <span style="color: #E0E0E0;">Se imparten a través de la plataforma Hotmart, con certificado oficial al finalizar.</span>
  </li>
  <li style="display: inline-flex; align-items: center; gap: 6px; margin-bottom: 10px; font-size: 18px; color: #81C784;">
    <span>☄️ </span>
    <span style="color: #E0E0E0;">Los módulos son descargables para estudiar a tu propio ritmo, con total flexibilidad.</span>
  </li>
  <li style="display: inline-flex; align-items: center; gap: 6px; font-size: 18px; color: #81C784;">
    <span>☄️ </span>
    <span style="color: #E0E0E0;">Además, cuentas con asesoría personalizada durante todo el curso.</span>
  </li>
</ul>

</div>

"""

    st.markdown(html_content, unsafe_allow_html=True)






    

 #Presentación de cursos con estrategia de marketing (descuentos limitados y prueba social)
    st.markdown("## 🎓 Cursos Disponibles")

    curso1, curso2, curso3 = st.columns(3)

    with curso1:
        st.image("https://img.freepik.com/vector-gratis/ecologia-estilo-vida-ecologico-personas-protegiendo-planeta_1150-39773.jpg", use_column_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.5); padding: 5px; border-radius: 10px;'>
            <h4>Estadística para el Análisis de Datos</h4>
            <p>Curso asincrónico con materiales descargables y marco legal completo según Ley Yolanda y Ley General del Ambiente.</p>
            <p><strong>ARS 12.000 / USD 49</strong></p>
            <h5 style='color: red;'>¡Accede al material exclusivo con tu inscripción!</h5>
            <p><strong>📌 Modalidad virtual – Plataforma Hotmart</strong></p>
            <p style='font-style: italic; color: #555;'>“Excelente curso, muy completo y claro. Lo recomiendo.” – Ana G.</p>
            <a href='https://go.hotmart.com/EJEMPLO1' target='_blank'>
                <button style='padding:8px 12px; background-color:#388E3C; color:white; border:none; border-radius:5px;'>¡Inscribirme ahora!</button>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with curso2:
        st.image("https://img.freepik.com/vector-gratis/gestion-residuos-ilustrado-contenedores_23-2148501732.jpg", use_column_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.5); padding: 5px; border-radius: 10px;'>
            <h4>Gestión de Residuos y Economía Circular</h4>
            <p>Capacitación técnica sobre clasificación, legislación vigente y estrategias de minimización en la industria y municipios.</p>
            <p><strong>ARS 14.000 / USD 59</strong></p>
            <h5 style='color: red;'>¡Accede al material exclusivo con tu inscripción!</h5>
            <p><strong>📌 Modalidad virtual – Plataforma Hotmart</strong></p>
            <p style='font-style: italic; color: #555;'>“Muy útil para mi trabajo en la municipalidad. Me encantó el enfoque práctico.” – Carlos D.</p>
            <a href='https://go.hotmart.com/EJEMPLO2' target='_blank'>
                <button style='padding:8px 12px; background-color:#388E3C; color:white; border:none; border-radius:5px;'>¡Inscribirme ahora!</button>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with curso3:
        st.image("https://img.freepik.com/vector-gratis/personas-protegiendo-planeta_23-2148510019.jpg", use_column_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.5); padding: 5px; border-radius: 10px;'>
            <h4>Ley Yolanda para Funcionarios Públicos</h4>
            <p>Capacitación obligatoria en educación ambiental con enfoque legal, social y técnico. Cumplí con la normativa vigente.</p>
            <p><strong>ARS 10.000 / USD 39</strong></p>
            <h5 style='color: red;'>¡Accede al material exclusivo con tu inscripción!</h5>
            <p><strong>📌 Modalidad virtual – Plataforma Hotmart</strong></p>
            <p style='font-style: italic; color: #555;'>“Fácil de seguir, con buena explicación legal. Ideal para funcionarios.” – Laura M.</p>
            <a href='https://go.hotmart.com/EJEMPLO3' target='_blank'>
                <button style='padding:8px 12px; background-color:#388E3C; color:white; border:none; border-radius:5px;'>¡Inscribirme ahora!</button>
            </a>
        </div>
        """, unsafe_allow_html=True)


    st.markdown("## 📬 ¿Te gustaría más información o recibir ofertas exclusivas?")

    # Formulario de contacto

    def es_correo_valido(correo):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, correo) is not None

    with st.form(key="formulario_contacto"):
        nombre = st.text_input("Nombre completo")
        correo = st.text_input("Correo electrónico")
        mensaje = st.text_area("Tu consulta o mensaje")
        acepto_marketing = st.checkbox("Acepto recibir correos electrónicos con novedades y ofertas.")
        
        enviar = st.form_submit_button(label="Enviar mensaje")

        if enviar:
            if not es_correo_valido(correo):
                st.warning("⚠️ Ingresá un correo electrónico válido.")
            elif not acepto_marketing:
                st.warning("⚠️ Para continuar, debes aceptar recibir correos electrónicos.")
            elif not nombre or not correo or not mensaje:
                st.warning("⚠️ Por favor completá todos los campos.")
            else:
                # Crear registro de datos
                nuevo_registro = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "nombre": nombre,
                    "correo": correo,
                    "mensaje": mensaje
                }

                # Guardar en archivo CSV
                archivo_csv = "leads_marketing.csv"
                if os.path.exists(archivo_csv):
                    df = pd.read_csv(archivo_csv)
                    df = pd.concat([df, pd.DataFrame([nuevo_registro])], ignore_index=True)
                else:
                    df = pd.DataFrame([nuevo_registro])

                df.to_csv(archivo_csv, index=False)
                st.success("✅ ¡Gracias! Hemos recibido tu mensaje y pronto te contactaremos.")
                
    # Luego el público objetivo con Markdown puro (para mejor soporte)
    st.markdown("""
    <div style='background-color: rgba(255, 255, 255, 0.4); padding: 5px; border-radius: 10px;'>
    <h2>👥 ¿A quiénes están dirigidos?</h2>

    <ul>
      <li>Estudiantes de carreras afines</li>
      <li>Docentes de todos los niveles</li>
      <li>Profesionales de la educación</li>
      <li>Funcionarios/as públicos/as (Ley Yolanda)</li>
      <li>Técnicos y profesionales en gestión ambiental</li>
      <li>Empresas y municipios en transición hacia la sostenibilidad</li>
      <li>Público en general interesado en las temáticas</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    

    # 📲 Botón flotante de WhatsApp
    st.markdown("""
        <a href='https://wa.me/+5493704003126' target='_blank'>
            <img src="https://img.lovepik.com/png/20231104/whatsapp-phone-icon-logo-whatsapp-digital-green_494222_wh860.png" alt="WhatsApp" width="60" height="60" style="position: fixed; bottom: 30px; right: 30px; border-radius: 50%; box-shadow: 0 0 10px rgba(0,0,0,0.2);"/>
        </a>
    """, unsafe_allow_html=True)
   
#------------------------
                
elif st.session_state.seccion == "Contacto":
    st.markdown("""
        <div style="padding: 0px; border-radius: 10px;">
        <h3 style="font-size: 28px;">📞 Contacto</h3>
        <p style="background-color: rgba(255, 255, 255, 0.4); font-size: 17px; padding: 10px; border-radius: 10px;">
        <strong>¿Tienes alguna consulta o te gustaría conocerme mejor?</strong> <br>
        Puedes contactarme por <strong>WhatsApp</strong>, <strong>correo electrónico</strong> o a través de <strong>LinkedIn</strong>. 
        También puedes explorar mis proyectos públicos en <strong>GitHub</strong>.<br>
        Encuentra todos los enlaces aquí:
        </p>
        </div>
    """, unsafe_allow_html=True)
    
    espacio1, col1, col2, col3, col4, espacio2 = st.columns([0.2, 0.8, 0.7, 0.67, 0.56, 0.1])


    # Mensaje para WhatsApp

    mensaje = "Hola, tengo una consulta sobre los servicios que ofreces."
    mensaje_codificado = urllib.parse.quote(mensaje)

# Tu número con código de país sin signos + ni espacios
    telefono = "5493704003126"

    whatsapp_link = f"https://wa.me/{telefono}?text={mensaje_codificado}"

    with col1:
        st.markdown(
            f'''
            <a href="{whatsapp_link}" target="_blank">
                <button style="background-color: #25D366; color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                    📱💬 Enviarme un WhatsApp
                </button>
            </a>
            ''',
            unsafe_allow_html=True
        )

    # Correo electrónico
    with col2:
        st.markdown(
            f'''
            <a href="mailto:berenice.ledesma12345@gmail.com">
                <button style="background-color: #4285F4; color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                    ✉️ Enviarme un correo
                </button>
            </a>
            ''',
            unsafe_allow_html=True
        )

    # LinkedIn
    linkedin_link = "https://www.linkedin.com/in/lara-berenice-l-89527332b/"
    with col3:
        st.markdown(
            f'''
            <a href="{linkedin_link}" target="_blank">
                <button style="background-color: #0077B5; color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                    🔗 Visita mi LinkedIn
                </button>
            </a>
            ''',
            unsafe_allow_html=True
        )

    # GitHub
    github_link = "https://github.com/LaraBerenice"
    with col4:
        st.markdown(
            f'''
            <a href="{github_link}" target="_blank">
                <button style="background-color: #24292E; color: white; font-weight: bold; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                    🐙 Visita mi GitHub
                </button>
            </a>
            ''',
            unsafe_allow_html=True
        )
    
  
# BLOG -----------------

fastapi_url = "http://127.0.0.1:8000"

if "mostrar_articulo" not in st.session_state:
    st.session_state.mostrar_articulo = False

elif st.session_state.seccion == "Blog":
    st.markdown('''
        <p style="background-color: rgba(255, 255, 255, 0.4); font-size: 17px; padding: 10px; border-radius: 10px;">
            ✍️ <strong>seleccioná un artículo:</strong>
        </p>
        ''', unsafe_allow_html=True)

    # Diccionario de títulos legibles y sus rutas/títulos codificados
    opciones = {
        "Cómo hacer un Plan de Negocio paso a paso": "plan_negocio",
        "Cómo usar el análisis de datos para tomar mejores decisiones en el agro": "articulo2",
        "¿Evaluar un proyecto de inversión agropecuaria: lo que necesitás saber antes de dar el paso": "articulo3"
    }

    articulo_legible = st.selectbox(
    "📚\u2003📚\u2003📚\u2003📖\u2003📚\u2003📚\u2003📖\u2003📚\u2003📚\u2003📖\u2003📚\u2003📚\u2003📖\u2003"
    "\u2003✨\u2003📖\u2003✨\u2003📖\u2003✨\u2003"
    "\u2003📖\u2003📚\u2003📚\u2003📖\u2003📚\u2003📚\u2003📖\u2003📚\u2003📚\u2003📖\u2003📚\u2003📚\u2003📖"
    "\u2003\u2003📚\u2003📖\u2003📚\u2003📖\u2003📚\u2003📚\u2003📖\u2003📚\u2003📖\u2003📚\u2003📚",
    list(opciones.keys())
)





    
    if st.button("📖 Ver artículo"):
        st.session_state.mostrar_articulo = True
    

    if st.session_state.mostrar_articulo:
        titulo_codificado = quote(opciones[articulo_legible])
        response = requests.get(f"{fastapi_url}/get_article?title={titulo_codificado}")
        
        if response.status_code == 200:
            imagenes = response.json()["imagenes"]
            for img_b64 in imagenes:
                st.image(f"data:image/jpeg;base64,{img_b64}")
        else:
            st.error("No se pudo cargar el artículo.")  


    
    