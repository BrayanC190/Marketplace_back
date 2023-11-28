from fastapi import FastAPI
import json
#from modelos.usuario import usuario
from funciones.usuarios import getUser as gu, updateUser as uu, createUser as cu


app = FastAPI()

"""
@app.get("/getUsers/{id}")
async def getUser(nickname:str):
    u = usuario()
    user = u.upload(f"{nickname}")
    #usuario_dict = user.to_dict()
    #usuario_json = json.dumps(usuario_dict)
    return {"prueba"}
"""

@app.get("/getUser/{nickname}")
async def getUser(nickname : str):
    usuario = gu(nickname)
    return usuario

@app.put("/updateUser/")
async def updateUser(nickname : str, telefono : str, calle1 : str, calle2 : str, colonia : str, lote : int, municipio : str, estado : str, pais : str):
    up = uu(nickname, telefono, calle1, calle2, colonia, lote, municipio, estado, pais)

@app.post("/createUser")
async def createUser(nickname : str, password :str, nombres : str, apellidoP : str, apellidoM :str, fechaN : str, correo : str):
    new = cu(nickname, password, nombres, apellidoP, apellidoM, fechaN, correo)

