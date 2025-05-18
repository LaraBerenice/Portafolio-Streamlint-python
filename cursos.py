import streamlit as st
import base64
import pandas as pd
from datetime import datetime
import os
import re

# Configuración de la página
st.set_page_config(page_title="Academia Ambiental - Cursos Online", layout="wide")

# 🌞🌙 Modo Día/Noche - inicialización
if 'mode' not in st.session_state:
    st.session_state.mode = "Modo Día"

# Encabezado con botones de modo
top_col1, top_col2 = st.columns([6, 1])
with top_col2:
    col_sol, col_luna = st.columns(2)
    with col_sol:
        if st.button("☀️"):
            st.session_state.mode = "Modo Día"
    with col_luna:
        if st.button("🌙"):
            st.session_state.mode = "Modo Noche"

modo = st.session_state.get("mode", "Modo Día")


# 🎨 Estilos por modo
if modo == "Modo Noche":
    st.markdown("""
        <style>
        .stApp {
            background-color: #2E2E2E;
            color: #FFFFFF;
        }
        .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader, .stCaption, .stCode {
            color: #FFFFFF !important;
        }
        .stButton>button {
            background-color: #333333;
            color: #FFFFFF;
            border: 1px solid #FFFFFF;
            font-weight: bold !important;
        }
        .stImage {
            border: none !important;
        }
        .profesora-info {
            background-color: #7A9D6B;  /* Verde oscuro */
            padding: 20px;
            color: #E8FFE8;
            border-radius: 5px;
            text-align: center;
            line-height: 1.8
        }
        /* Campos del formulario */
        input, textarea, label, .stCheckbox > div {
            color: black !important;
        }
        /* Cambiar el color de fondo del formulario */
        .stForm {
            background-color: #7A9D6B;!important;  /* Color gris claro */
            padding: 20px;  /* Opcional, agrega espacio alrededor del formulario */
            border-radius: 10px;  /* Opcional, bordes redondeados */
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: #A8D08D;
            color: #006400;
        }
        .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader, .stCaption, .stCode {
            color: #333333 !important;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: 1px #4CAF50 solid;
            font-weight: bold !important;
        }
        .stImage {
            border: 2px solid #00000000;
        }
        .profesora-info {
            background-color: #4CAF50;  /* Verde claro */
            padding: 20px;
            color: #2F4F2F;
            border-radius: 5px;
            text-align: center;
            line-height: 1.8
        }
        /* Campos del formulario */
        input, textarea, label, .stCheckbox > div {
            color: black !important;
        }
         /* Cambiar el color de fondo del formulario */
        .stForm {
            background-color: #4CAF50;!important;  /* Color  */
            padding: 20px;  /* Opcional, agrega espacio alrededor del formulario */
            border-radius: 10px;  /* Opcional, bordes redondeados */

        </style>
    """, unsafe_allow_html=True)


#---------------------------------------------------------------

# Título principal con identidad profesional
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🌿 Capacitaciones especializadas en ambiente, agro y herramientas transversales</h1>
    <p style='text-align: center; font-size: 20px;'>
        Formación continua con aval profesional y respaldo legal
    </p>
    <hr style='border: 1px solid #4CAF50;'/>
""", unsafe_allow_html=True)


# Perfil profesional

modo_actual = "modo-noche" if st.session_state.mode == "Modo Noche" else "modo-dia"

st.markdown(f"""
  <div class="profesora-info {modo_actual}">
    <p>
        Formaciones adaptadas a distintas necesidades en temáticas ambientales y agropecuarias, complementadas con herramientas prácticas aplicables tanto a disciplinas agroambientales como a otros campos científicos.<br><br>
        Los contenidos están diseñados para fortalecer <strong>capacidades técnicas, analíticas y de gestión</strong>.
        Los cursos se imparten a través de <strong>Hotmart</strong>, donde podrás obtener un <strong>certificado</strong> al finalizar. Además, tendrás acceso para descargar los módulos y estudiar a tu propio ritmo, de manera cómoda. También contarás con <strong>asesoría personalizada del profesional durante la duracion del curso. </strong> 
    </p>
</div>
""", unsafe_allow_html=True)


#---------------------------------------------------------------

# Marco legal
with st.expander("📜 Aval y Marco Legal de los Cursos sobre temáticas agroambientales"):
    st.markdown("""
                
Los cursos se dictan en el marco del ejercicio profesional autorizado por la matrícula correspondiente, y están amparados por:

- Ley 25.675 – Ley General del Ambiente  
- Ley 27.592 – Ley Yolanda  
- Ley 27.621 – Ley de Educación Ambiental Integral  

La formación se brinda dentro del campo de competencia profesional, conforme a la normativa vigente.

""")

# Presentación de cursos con estrategia de marketing (descuentos limitados y prueba social)
st.markdown("## 🎓 Cursos Disponibles")

cursos = [
    {
        "titulo": "Estadística para el Análisis de Datos ",
        "descripcion": "Curso asincrónico con materiales descargables y marco legal completo según Ley Yolanda y Ley General del Ambiente.",
        "imagen": "https://img.freepik.com/vector-gratis/ecologia-estilo-vida-ecologico-personas-protegiendo-planeta_1150-39773.jpg",
        "precio": "ARS 12.000 / USD 49",
        "descuento": "¡Accede al material exclusivo con tu inscripción!",
        "enlace": "https://go.hotmart.com/EJEMPLO1",
        "testimonio": "“Excelente curso, muy completo y claro. Lo recomiendo.” – Ana G."
    },
    {
        "titulo": "Gestión de Residuos y Economía Circular",
        "descripcion": "Capacitación técnica sobre clasificación, legislación vigente y estrategias de minimización en la industria y municipios.",
        "imagen": "https://img.freepik.com/vector-gratis/gestion-residuos-ilustrado-contenedores_23-2148501732.jpg",
        "precio": "ARS 14.000 / USD 59",
        "descuento": "¡Accede al material exclusivo con tu inscripción!",
        "enlace": "https://go.hotmart.com/EJEMPLO2",
        "testimonio": "“Muy útil para mi trabajo en la municipalidad. Me encantó el enfoque práctico.” – Carlos D."
    },
    {
        "titulo": "Ley Yolanda para Funcionarios Públicos",
        "descripcion": "Capacitación obligatoria en educación ambiental con enfoque legal, social y técnico. Cumplí con la normativa vigente.",
        "imagen": "https://img.freepik.com/vector-gratis/personas-protegiendo-planeta_23-2148510019.jpg",
        "precio": "ARS 10.000 / USD 39",
        "descuento": "¡Accede al material exclusivo con tu inscripción!",
        "enlace": "https://go.hotmart.com/EJEMPLO3",
        "testimonio": "“Fácil de seguir, con buena explicación legal. Ideal para funcionarios.” – Laura M."
    }
]

cols = st.columns(3)

for i, curso in enumerate(cursos):
    with cols[i]:
        st.image(curso["imagen"], use_column_width=True)
        st.subheader(curso["titulo"])
        st.markdown(f"**{curso['precio']}**")
        st.write(curso["descripcion"])
        st.markdown(f"<h4 style='color: red;'>{curso['descuento']}</h4>", unsafe_allow_html=True)
        st.markdown("<p><strong>📌 Modalidad virtual – Plataforma Hotmart</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-style: italic; color: #555;'>{curso['testimonio']}</p>", unsafe_allow_html=True)
        st.markdown(
            f"<a href='{curso['enlace']}' target='_blank'>"
            "<button style='background-color: #388E3C; color: white; padding: 10px 20px; border: none; border-radius: 6px;'>"
            "¡Inscribirme ahora!</button></a>", 
            unsafe_allow_html=True
        )

# Prueba social: Testimonios
st.markdown("## 🗣️ Testimonios de Estudiantes")
st.markdown("""
> "El curso de Ley Yolanda me permitió comprender los aspectos legales y cómo implementarlos en mi trabajo como funcionario público. ¡Muy útil!"  
> *Ana Pérez, Funcionaria Pública*

> "La capacitación en Gestión de Residuos me ayudó a desarrollar proyectos más sostenibles y a aplicar la normativa en mi empresa agroindustrial."  
> *Juan Rodríguez, Técnico en Agroindustria*

> "Gracias al taller de Evaluación de Impacto Ambiental, logré integrar mejor los criterios ambientales en mis informes técnicos."  
> *María Gómez, Consultora Ambiental*

> "Excelente nivel docente y contenido actualizado. Me sirvió muchísimo para presentarme a licitaciones con requisitos ambientales."  
> *Carlos Méndez, Ingeniero Civil*
""")

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

# Urgencia de inscripción
st.markdown("""
### ⚠️ ¡Última oportunidad!  
Solo quedan **10 plazas** para el curso de **Educación Ambiental**. ¡Aprovechá antes de que se agoten!
""")

# Público objetivo
st.markdown("""
## 👥 ¿A quiénes están dirigidos?

- Estudiantes de carreras afines
- Docentes de todos los niveles
- Profesionales de la educación
- Funcionarios/as públicos/as (Ley Yolanda)
- Técnicos y profesionales en gestión ambiental  
- Empresas y municipios en transición hacia la sostenibilidad
- Público en general interesado en las temáticas

""")

# 📲 Botón flotante de WhatsApp
st.markdown("""
    <a href='https://wa.me/+5493704003126' target='_blank'>
        <img src="https://img.lovepik.com/png/20231104/whatsapp-phone-icon-logo-whatsapp-digital-green_494222_wh860.png" alt="WhatsApp" width="60" height="60" style="position: fixed; bottom: 30px; right: 30px; border-radius: 50%; box-shadow: 0 0 10px rgba(0,0,0,0.2);"/>
    </a>
""", unsafe_allow_html=True)

