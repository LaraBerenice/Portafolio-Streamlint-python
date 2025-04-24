# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pdf2image import convert_from_path
import os
from urllib.parse import quote
import base64
from io import BytesIO
from PIL import Image


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_article")
def get_article(title: str):
    nombre_archivo = f"{title}.pdf"
    ruta_archivo = os.path.join("articulos", nombre_archivo)

    if not os.path.exists(ruta_archivo):
        return JSONResponse(content={"error": "Archivo no encontrado"}, status_code=404)

    try:
        imagenes = convert_from_path(ruta_archivo, dpi=150)
        imagenes_base64 = []

        for img in imagenes:
            # Convertir a RGBA para permitir transparencia
            img = img.convert("RGBA")
            datas = img.getdata()

            newData = []
            for item in datas:
                # Si el píxel es blanco, hacerlo transparente
                if item[:3] == (255, 255, 255):
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            img.putdata(newData)

            buffer = BytesIO()
            img.save(buffer, format="PNG")  # Usamos PNG
            img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
            imagenes_base64.append(img_b64)

        return {"imagenes": imagenes_base64}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)