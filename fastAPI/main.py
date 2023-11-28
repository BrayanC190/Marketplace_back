from fastapi import FastAPI
import json
from modelos.usuario import usuario


app = FastAPI()

@app.get("/getUser/{id}")
async def getUser(nickname:str):
    u = usuario()
    user = u.upload(f"{nickname}")
    #usuario_dict = user.to_dict()
    #usuario_json = json.dumps(usuario_dict)
    return {"prueba"}