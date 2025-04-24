import streamlit as st
import base64
import urllib.parse
import requests
from urllib.parse import quote

# Configuración de la página
st.set_page_config(page_title="Análisis de Datos, Agronegocios y Gestión Ambiental", layout="wide")

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
        st.image(logo, width=400)
    with col_desc:
        st.write("")
        st.write("")
        st.write("")
        st.markdown("""
        <div>
            <h3 style="font-size: 55px;">
            📊 Agronegocios, Gestión Ambiental y Análisis de Datos 🌱
            </h3>
        </div>
            """, unsafe_allow_html=True)


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
            font-weight: bold !important;
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
            border: 1px #4CAF50 solid;
            font-weight: bold !important;
            font-size: 15px !important;
        }}
        .stImage {{
            border: 2px solid #00000000;
        }}
        </style>
    """, unsafe_allow_html=True)


# Columnas para navegación centrada
# Crear espacio en blanco a los costados para centrar los botones
espacio_izquierda, nav1, nav2, nav3, nav4, espacio_derecha = st.columns([2.2, 0.8, 0.8, 0.6, 0.7, 2])

with nav1:
    if st.button("Servicios"):
        st.session_state.seccion = "Servicios"

with nav2:
    if st.button("Proyectos"):
        st.session_state.seccion = "Proyectos"

with nav3:
    if st.button(" Blog "):
        st.session_state.seccion = "Blog"

with nav4:
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
    <div style='text-align: center; margin-top: 30px; background-color: rgba(255,255,255,0.8); padding: 15px; border-radius: 12px;'>
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
            <h4>Utilizando hojas de cálculo:</h4>
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
    <div style="background-color: rgba(255, 255, 255, 0.4); padding: 15px; border-radius: 12px;">
        <p><strong>👩‍🌾 💬María G. (Productora agrícola):</strong> "El análisis de costos que me preparaste me ayudó a optimizar los gastos en la producción. ¡Gracias por tu dedicación!"</p>
        <p><strong>👨‍💼 💬 Pablo R. (Emprendedor):</strong> "Con tu plan de negocios pude conseguir el crédito que necesitaba. Excelente acompañamiento."</p>
        <p><strong>👩‍🔬 💬Laura M. (Ingeniera ambiental):</strong> "Tu diagnóstico fue clave para mejorar nuestros indicadores de impacto. ¡Gran profesionalismo y claridad técnica!"</p>
        <p><strong>👨‍🌍 💬 Diego F. (Consultor en sostenibilidad):</strong> "Gracias a tu asesoramiento, pudimos diseñar una estrategia ambiental más efectiva para nuestros clientes."</p>
        <p><strong>👩‍💻 💬 Sofía T. (Analista de datos):</strong> "El dashboard que desarrollaste fue justo lo que necesitábamos para tomar decisiones más informadas. Muy recomendable."</p>
    </div>
    """, unsafe_allow_html=True)

#---------------------------------
# BLOG -----------------

fastapi_url = "http://127.0.0.1:8000"

if "mostrar_articulo" not in st.session_state:
    st.session_state.mostrar_articulo = False

elif st.session_state.seccion == "Blog":
    st.markdown("### ✍️ Artículos: ")

    # Diccionario de títulos legibles y sus rutas/títulos codificados
    opciones = {
        "Cómo hacer un Plan de Negocio paso a paso": "plan_negocio",
        "5 indicadores clave para el control de gestión": "5 indicadores clave para el control de gestión",
        "¿Por qué es importante el análisis de datos en los agronegocios?": "¿Por qué es importante el análisis de datos en los agronegocios?"
    }

    articulo_legible = st.selectbox("📚 Seleccioná un artículo:", list(opciones.keys()))

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


#------------------------
                
elif st.session_state.seccion == "Contacto":
    st.markdown("""
        <div style="padding: 0px; border-radius: 10px;">
        <h3 style="font-size: 28px;">📞 Contacto</h3>
        <p style="background-color: rgba(255, 255, 255, 0.4); font-size: 17px; padding: 10px; border-radius: 10px;">
        <strong>¿Tienes alguna consulta o te gustaría conocerme mejor?</strong> <br>
        Puedes contactarme a través de <strong>WhatsApp</strong>, <strong>correo
        electrónico</strong>, verme o escribirme en <strong>LinkedIn</strong>,
        o explorar mis proyectos públicos en <strong>GitHub</strong>.<br>
        Todos los enlaces aquí:
        </p>

        </div>
    """, unsafe_allow_html=True)


    col1, col2, col3, col4 = st.columns(4)


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