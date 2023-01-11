from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# inicia el server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users = [User(name = "Brais",surname = "Moure", url = "https://moure.dev",age = 35),
         User(name = "Pepe",surname = "González",url = "https://www.auyantepui.com",age = 40),
         User(name = "Gema",surname = "Guerra",url = "https://www.valoren.es",age = 30)]    


@app.get("/usuariosjson")
async def jsonusuarios():
    return users

@app.get("/usuarios")
async def usuarios():
    return [{"name": "Gema", "surname": "Guerra", "url": "https://www.valoren.es", "age": 40},
            {"name": "Pepe", "surname": "González", 
                "url": "https://www.auyantepui.com", "age": 30},
            {"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 20}]

