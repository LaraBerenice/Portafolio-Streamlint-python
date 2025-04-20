import streamlit as st
import base64

# Configuración de la página
st.set_page_config(page_title="Servicios Ambientales", layout="wide")

def imagen_base64(ruta):
    with open(ruta, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64}"

# Modo Día/Noche (debe inicializarse primero)
if 'mode' not in st.session_state:
    st.session_state.mode = "Modo Día"

# Línea superior con logo + descripción a la izquierda y sol/luna a la derecha
top_col1, top_col2 = st.columns([6, 1])  # Más espacio a la izquierda

with top_col1:
    col_logo, col_desc = st.columns([1, 3])
    with col_logo:
        logo = imagen_base64("Imagenes/logo.png")
        st.image(logo, width=500)
    with col_desc:
        st.write("")
        st.write("")
        st.markdown("""
            ### 📊 Agronegocios | Gestión Ambiental | Análisis de Datos🌱
            Ledesma Lara Berenice -
            Licenciada en Gestión de Agroempresas & Estudiante de Maestría en Gestión Ambiental
        """)

with top_col2:
    col_sol, col_luna = st.columns(2)
    with col_sol:
        if st.button("☀️"):
            st.session_state.mode = "Modo Día"
    with col_luna:
        if st.button("🌙"):
            st.session_state.mode = "Modo Noche"

# Cambiar estilos según el modo
if st.session_state.mode == "Modo Noche":
    fondo = imagen_base64("Imagenes/Campo nocturno bajo la luna llena.png")
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: #121212;
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
        }}
        .stImage {{
            border: none !important;
        }}
        </style>
    """, unsafe_allow_html=True)
else:
    fondo = imagen_base64("Imagenes/Campo agrícola y paneles solares.png")
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: #FFFFFF;
            color: #006400;
            background-image: url('{fondo}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader, .stCaption, .stCode {{
            color: #000000 !important;
        }}

        .stButton>button {{
            background-color: #4CAF50;
            color: white;
            border: none;
        }}
        .stImage {{
            border: 2px solid #00000000;
        }}
        </style>
    """, unsafe_allow_html=True)


# Barra de navegación centrada
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns([2, 1, 1, 1, 2])  # Espacios a los lados para centrar

with nav_col2:
    if st.button("Servicios"):
        st.session_state.seccion = "Servicios"
with nav_col3:
    if st.button("Proyectos"):
        st.session_state.seccion = "Proyectos"
with nav_col4:
    if st.button("Contacto"):
        st.session_state.seccion = "Contacto"

# Inicializar sección si no está definida
if 'seccion' not in st.session_state:
    st.session_state.seccion = "Servicios"

# CONTENIDO DE CADA SECCIÓN
if st.session_state.seccion == "Servicios":
    st.markdown("### 💼 Servicios")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image("https://picsum.photos/400/300?random=1", use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.4); padding: 15px; border-radius: 10px;'>
            <h4>Plan de Negocio</h4>
            <p>Documento fundamental para organizar, estructurar y comunicar una idea de negocio. Contiene el análisis del entorno, definición de objetivos, estructura organizativa, estrategias operativas, y puede incorporar el plan de marketing, evaluación de inversiones y análisis de costos. Es ideal para presentar ante socios, inversores o instituciones de financiamiento.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("https://picsum.photos/400/300?random=2", use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.85); padding: 15px; border-radius: 10px;'>
            <h4>Plan de Marketing</h4>
            <p>Puede integrarse al plan de negocios o desarrollarse de manera independiente. Define las estrategias para posicionar productos o servicios en el mercado, identificando al público objetivo, canales de comunicación y acciones promocionales.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.image("https://picsum.photos/400/300?random=3", use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.85); padding: 15px; border-radius: 10px;'>
            <h4>Evaluación de Proyectos de Inversión</h4>
            <p>Análisis financiero que permite estimar la viabilidad y rentabilidad de un proyecto. Puede formar parte del plan de negocios o utilizarse como documento técnico específico para decisiones de inversión.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.image("https://picsum.photos/400/300?random=4", use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.85); padding: 15px; border-radius: 10px;'>
            <h4>Análisis de Costos</h4>
            <p>Estudio detallado de la estructura de costos de una empresa o proyecto. Permite identificar márgenes, optimizar recursos y calcular precios de venta.</p>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.image("https://picsum.photos/400/300?random=4", use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.85); padding: 15px; border-radius: 10px;'>
            <h4>Dashboards de Control de Gestión</h4>
            <p>Complemento visual y dinámico para todos los documentos anteriores. Desarrollo tableros interactivos que permiten monitorear indicadores clave (KPI), visualizar tendencias y facilitar la toma de decisiones.</p>
        </div>
        """, unsafe_allow_html=True)

#-----------
# SECCIÓN PROYECTOS
elif st.session_state.seccion == "Proyectos":    
    st.markdown("### 🚀 Proyectos")
    col6, col7, col8 = st.columns(3)
    
    with col6:
        st.image("https://picsum.photos/400/300?random=5", use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.85); padding: 15px; border-radius: 10px;'>
            <h4>Proyecto de Evaluación Ambiental</h4>
            <p>Recomendaciones para la mejora en la sostenibilidad.</p>
            <a href="https://enlace-a-tu-proyecto-1.com">Ver más sobre el Plan de Gestión de Residuos</a>
        </div>
        """, unsafe_allow_html=True)

    with col7:
        st.image("https://picsum.photos/400/300?random=6", use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.85); padding: 15px; border-radius: 10px;'>
            <h4>Plan de Gestión de Residuos</h4>
            <p>Reducción del impacto ambiental agroindustrial.</p>
            <a href="https://enlace-a-tu-proyecto-2.com">Ver más sobre el Plan de Gestión de Residuos</a>
        </div>
        """, unsafe_allow_html=True)

    with col8:
        st.image("https://picsum.photos/400/300?random=7", use_container_width=True)
        st.markdown("""
        <div style='background-color: rgba(255, 255, 255, 0.85); padding: 15px; border-radius: 10px;'>
            <h4>Optimización de Recursos</h4>
            <p>Gestión eficiente de recursos naturales.</p>
            <a href="https://enlace-a-tu-proyecto-3.com">Ver más sobre el Plan de Gestión de Residuos</a>
        </div>
        """, unsafe_allow_html=True)

        
elif st.session_state.seccion == "Contacto":
    st.markdown("### 📞 Contacto")
    st.write("¿Tienes alguna consulta o te gustaría conocerme más? Puedes contactarme por WhatsApp, email, escribirme y verme en LinkedIn, o ver mis proyectos en GitHub. ¡Estoy a tu disposición!")

    col1, col2, col3, col4 = st.columns(4)

    whatsapp_link = "https://wa.me/5491234567890?text=Hola,%20tengo%20una%20consulta%20sobre%20tus%20servicios%20ambientales"
    with col1:
        if st.button("Enviar WhatsApp"):
            st.write(f"[Haz clic aquí para hablar por WhatsApp]( {whatsapp_link} )")

    with col2:
        if st.button("Enviar un correo"):
            st.write("¡Correo enviado!")

    github_link = "https://github.com/tu-usuario"
    with col3:
        if st.button("Visita nuestro GitHub"):
            st.write(f"[GitHub]( {github_link} )")

    linkedin_link = "https://www.linkedin.com/in/tu-usuario"
    with col4:
        if st.button("Visita nuestro LinkedIn"):
            st.write(f"[LinkedIn]( {linkedin_link} )")
