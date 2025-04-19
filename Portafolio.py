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
        logo = imagen_base64("Imagenes/Logo2.png")
        st.image(logo, width=500)
    with col_desc:
        st.write("")
        st.write("")
        st.write("")
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
            color: #000000;
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
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://picsum.photos/400/300?random=1", use_container_width=True)
        st.markdown("### Estudios de Impacto Ambiental (EIA)")
        st.write("Evaluación completa del impacto ambiental de proyectos agrícolas o industriales.")
    with col2:
        st.image("https://picsum.photos/400/300?random=2", use_container_width=True)
        st.markdown("### Gestión de residuos agroindustriales")
        st.write("Planes sostenibles para residuos sólidos y líquidos.")
    with col3:
        st.image("https://picsum.photos/400/300?random=3", use_container_width=True)
        st.markdown("### Análisis de datos ambientales")
        st.write("Interpretación de datos para decisiones sostenibles.")
    with col4:
        st.image("https://picsum.photos/400/300?random=4", use_container_width=True)
        st.markdown("### Certificaciones y normativas")
        st.write("Asesoramiento para cumplir con normativas.")

elif st.session_state.seccion == "Proyectos":
    st.markdown("### 🚀 Proyectos")
    col5, col6, col7 = st.columns(3)
    with col5:
        st.image("https://picsum.photos/400/300?random=5", use_container_width=True)
        st.markdown("### Proyecto de Evaluación Ambiental")
        st.write("Recomendaciones para la mejora en la sostenibilidad.")
        st.markdown("[Ver más sobre el Plan de Gestión de Residuos](https://enlace-a-tu-proyecto-1.com)")
    with col6:
        st.image("https://picsum.photos/400/300?random=6", use_container_width=True)
        st.markdown("### Plan de Gestión de Residuos")
        st.write("Reducción del impacto ambiental agroindustrial.")
        st.markdown("[Ver más sobre el Plan de Gestión de Residuos](https://enlace-a-tu-proyecto-2.com)")
    with col7:
        st.image("https://picsum.photos/400/300?random=7", use_container_width=True)
        st.markdown("### Optimización de Recursos")
        st.write("Gestión eficiente de recursos naturales.")
        st.markdown("[Ver más sobre el Plan de Gestión de Residuos](https://enlace-a-tu-proyecto-3.com)")

elif st.session_state.seccion == "Contacto":
    st.markdown("### 📞 Contacto")
    st.write("¿Tenés alguna consulta o querés discutir un proyecto? ¡Contactanos!")

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
