from fastapi import FastAPI



app = FastAPI()





@app.get("/")
def index ():
    return {"¡¿Que ondaaaaaa?!" : "Hola, Mundo"}


@app.get("/libros/{id}")
def getBOOKS (id: int):
    return {"data": id}


