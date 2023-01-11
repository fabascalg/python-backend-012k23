from fastapi import FastAPI

app = FastAPI()

# inicia el server: uvicorn users:app --reload


@app.get("/users")
async def usuarios():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev"},
            {"name": "Pepe", "surname": "González",
                "url": "https://www.auyantepui.com"},
            {"name": "Gema", "surname": "Guerra", "url": "https://www.valoren.es"}]
