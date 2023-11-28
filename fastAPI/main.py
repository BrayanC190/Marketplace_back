from fastapi import FastAPI
import json
#from modelos.usuario import usuario
from funciones.usuarios import getUser as gu, updateUser as uu, createUser as cu, validateLogin as vl
from funciones.usuarios import credenciales as lu, updateDatos as ud, newDatos as nd
from funciones.smallpublicaciones import getSmallPublicaciones as sp


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
@app.post("/login")
def login(crendeciales : lu):
    valid = vl(crendeciales.nickname, crendeciales.password)
    if (valid): return {"msg":"usuario valido"}
    else : return {"msg" : "usuario invalido", "user":crendeciales.nickname, "pass":crendeciales.password}

@app.get("/getUser/{nickname}")
async def getUser(nickname : str):
    usuario = gu(nickname)
    return usuario

@app.put("/updateuser")
def updateUser(datos : ud):
    up = uu(datos.nickname, datos.telefono, datos.calle1, datos.calle2, datos.colonia, datos.lote, datos.municipio, datos.estado, datos.pais)

@app.post("/createuser")
def createUser(cuenta : nd):
    new = cu(cuenta.nickname, cuenta.password, cuenta.nombres, cuenta.apellidoP, cuenta.apellidoM, cuenta.fechaN, cuenta.correo)


@app.get("/getSmallPublicaciones/")
async def getSmallPublicaciones():
    sp = getSmallPublicaciones()
    return sp