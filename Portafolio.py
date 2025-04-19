import streamlit as st

st.set_page_config(page_title="Portafolio Profesional", layout="wide")

# --- Perfil ---
st.title("Lic. en Gestión Ambiental | Analista de Datos")
st.write("""
Soy especialista en medio ambiente y análisis de datos. 
Ayudo a empresas del sector agropecuario a cumplir con normativas ambientales 
y tomar decisiones sostenibles mediante herramientas técnicas y datos.
""")

# --- Servicios ---
st.header("Servicios")
st.write("""
- Elaboración de Informes de Impacto Ambiental (EIA)  
- Planes de Gestión de Residuos  
- Monitoreo y diagnóstico ambiental  
- Análisis de datos ambientales y visualización técnica
""")

# --- Proyectos ---
st.header("Proyectos")
st.subheader("Proyecto 1: Diagnóstico ambiental en zona rural")
st.write("Estudio sobre calidad del suelo y gestión de residuos en campos agrícolas.")
st.markdown("[Ver en GitHub](https://github.com/tu_usuario/proyecto1)")

st.subheader("Proyecto 2: Visualización de datos de impacto ambiental")
st.write("Dashboard interactivo para analizar indicadores de impacto en agroindustrias.")
st.markdown("[Ver en GitHub](https://github.com/tu_usuario/proyecto2)")

# --- Contacto ---
st.header("Contacto")
st.write("Podés encontrarme en:")
st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/tu_usuario)  
- [GitHub](https://github.com/tu_usuario)  
- Correo: tuemail@gmail.com
""")

# --- WhatsApp ---
whatsapp_url = "https://wa.me/5493704001234?text=Hola%2C+me+interesa+tu+servicio+de+consultor%C3%ADa+ambiental"
st.markdown(f"**[Contactame directamente por WhatsApp]({whatsapp_url})**", unsafe_allow_html=True)
