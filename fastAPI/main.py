from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
#from modelos.usuario import usuario
from funciones.usuarios import getUser as gu, updateUser as uu, createUser as cu, validateLogin as vl
from funciones.usuarios import credenciales as lu, updateDatos as ud, newDatos as nd
from funciones.smallpublicaciones import getSmallPublicaciones as sp
from funciones.allpublicaciones import getAllPublicaciones as ap

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origins
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

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
    print(nickname)
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
    pub = sp()
    return pub

@app.get("/getAllPublicaciones/{idPublicacion}")
async def getAllPublicaciones(idPublicacion : int):
    publicacion = ap(idPublicacion)
    return publicacion