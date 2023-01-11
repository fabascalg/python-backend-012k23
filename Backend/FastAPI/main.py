from fastapi import FastAPI

app = FastAPI()

# mapeo a raiz
@app.get("/")
def root():
    return "¡Hola FastAPI! Aquí probando --reload"

# mapeo a /url
@app.get("/url")
def url():
    return {"url": "https://mouredev.com/python"}

# Iniciar el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# PostMan




