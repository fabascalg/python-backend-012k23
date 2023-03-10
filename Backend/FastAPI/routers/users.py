from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

router = APIRouter()

# documentación con Swagger: http://localhost:8000/docs
# documentación con Redocly: http://localhost:8000/redoc

# inicia el server: uvicorn users:app --reload

# Entidad User


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


# lista de instancias de entidad User
users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="Pepe", surname="González",
                   url="https://www.auyantepui.com", age=40),
              User(id=3, name="Gema", surname="Guerra", url="https://www.valoren.es", age=30)]


# devuelve toda la lista de usuarios
@router.get("/usuarios")
async def usuarios():
    return users_list

# @router.get("/usuariosjson")
# async def jsonusuarios():
#    return [{"name": "Gema", "surname": "Guerra", "url": "https://www.valoren.es", "age": 40},
#            {"name": "Pepe", "surname": "González",
#                "url": "https://www.auyantepui.com", "age": 30},
#            {"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 20}]

# se puede escribir con el mismo nombre, el servidor distingue la
# petición según sea por path o por query
# ¿¿¿aquí también se llama sobrecarga???

# petición por path // devuelve un usuario por id
# si se envía sin id, el programa responde que falta un campo!!!


@router.get("/usuario/{id}")
async def usuario(id: int):
    return search_user(id)

# petición por query // igual devuelve el usuario por id, aunque esta vez
# ej: http://127.0.0.1:8000/usuarioconsulta/?id=3 si se pasan mas parámetros de esta forma se separan con '&'
# userquery es como lo ha llamado Moure...


@router.get("/usuario/")
async def usuario(id: int):
    return search_user(id)

# añadir un usuario a la lista, revisando que el id no exista previamente!!! OJO FALLA


@router.post("/usuario/", response_model=User, status_code=201)
async def usuario(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    users_list.append(user)
    return user


@router.put("/usuario/")
async def usuario(user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return user
    return {"error": "No se ha actualizado el usuario"}

# la misma función trabaja para petición por path de id o por query... o para verificar que el usuario existe previamente... en el caso de querer añadir


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "no se ha encontrado al usuario"}


@router.delete("/usuario/{id}")
async def user(id: int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            return {"message": "se ha eliminado el usuario"}
    return {"message": "no se encontro el usuario a eliminar"}
