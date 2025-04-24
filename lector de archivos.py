elif st.session_state.seccion == "Blog":
    st.markdown("### ✍️ Artículos de interés")
    
    def mostrar_pdf(pdf_path):
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'''
                <iframe src="data:application/pdf;base64,{base64_pdf}" width="1210" height="1000" type="application/pdf"></iframe>
            '''
            st.markdown(pdf_display, unsafe_allow_html=True)

    opciones = {
        "Cómo hacer un Plan de Negocio paso a paso": "articulos/plan_negocio.pdf",
        "5 indicadores clave para el control de gestión": "articulos/indicadores_clave.pdf",
        "¿Por qué es importante el análisis de datos en los agronegocios?": "articulos/analisis_datos_agro.pdf"
    }

    articulo = st.selectbox("📚 Seleccioná un artículo:", list(opciones.keys()))

    if st.button("📖 Ver artículo"):
        mostrar_pdf(opciones[articulo])