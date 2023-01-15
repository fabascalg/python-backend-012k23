from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# inicia el server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id = 1, name = "Brais",surname = "Moure", url = "https://moure.dev",age = 35),
         User(id = 2, name = "Pepe",surname = "González",url = "https://www.auyantepui.com",age = 40),
         User(id = 3, name = "Gema",surname = "Guerra",url = "https://www.valoren.es",age = 30)]    


@app.get("/usuariosjson")
async def jsonusuarios():
    return users_list

@app.get("/usuarios")
async def usuarios():
    return [{"name": "Gema", "surname": "Guerra", "url": "https://www.valoren.es", "age": 40},
            {"name": "Pepe", "surname": "González", 
                "url": "https://www.auyantepui.com", "age": 30},
            {"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 20}]

# se puede escribir con el mismo nombre, el servidor distingue la 
# petición según sea por path o por query
# ¿¿¿aquí también se llama sobrecarga???

# petición por path
@app.get("/usuario/{id}")
async def usuario(id: int):
    return search_user(id)

# petición por query
# ej: http://127.0.0.1:8000/usuarioconsulta/?id=3
# userquery es como lo ha llamado Moure...
@app.get("/usuario/")
async def usuario(id: int):
    return search_user(id)

@app.post("/usuario/")
async def usuario(user: User):
    if type(search_user(user.id)) == user:
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)

@app.put("/usuario/")
async def usuario(user: User):
    Found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            Found = True
    if not Found:
        return {"error": "No se ha actualizado el usuario"}
        



# la misma función trabaja para petición por path de id o por query...
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "no se ha encontrado el usuario"}


