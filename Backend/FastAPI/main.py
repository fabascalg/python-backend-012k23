from fastapi import FastAPI
from routers import products, users

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

# mapeo a raiz
@app.get("/")
def root():
    return "¡Hola FastAPI! Aquí probando --reload"

# mapeo a /url
@app.get("/url")
def url():
    return {"url": "https://mouredev.com/python"}

@app.get("/sumar/{operador1}/{operador2}")
def sumar(operador1: int,operador2: int):
    return operador1 + operador2

# Iniciar el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# PostMan

# hemos añadido Thunder Client a VSC para procesar peticiones a servidor



