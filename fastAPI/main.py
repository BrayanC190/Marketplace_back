from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from funciones.usuarios import *
from funciones.publicaciones import *

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origins
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

@app.post("/login")
def e_login(e_crendeciales : credenciales):
    valid = validateLogin(e_crendeciales.nickname, e_crendeciales.password)
    if (valid): return {"msg":"usuario valido"}
    else : return {"msg" : "usuario invalido", "user":e_crendeciales.nickname, "pass":e_crendeciales.password}

@app.get("/getUser/{nickname}")
async def e_getUser(nickname : str):
    usuario = getUser(nickname)
    return usuario

@app.put("/updateuser")
def e_updateUser(e_datos : updateDatos):
    up = updateUser(e_datos.nickname, e_datos.telefono, e_datos.calle1, e_datos.calle2, e_datos.colonia, e_datos.lote, e_datos.municipio, e_datos.estado, e_datos.pais)

@app.post("/createuser")
def e_createUser(e_cuenta : newDatos):
    new = createUser(e_cuenta.nickname, e_cuenta.password, e_cuenta.nombres, e_cuenta.apellidoP, e_cuenta.apellidoM, e_cuenta.fechaN, e_cuenta.correo)


@app.get("/getSmallPublicaciones/")
async def e_getSmallPublicaciones():
    pub = getSmallPublicaciones()
    return pub

@app.get("/getAllPublicaciones/{idPublicacion}")
async def e_getAllPublicaciones(idPublicacion : int):
    publicacion = getAllPublicaciones(idPublicacion)
    return publicacion

@app.get("/getGuardados{nickname}")
async def e_getGuardados(nickname : str):
    guardados = getGuardados(nickname)
    return guardados

@app.post("/newGuardado")
async def e_newGuardado(datos : datosGuardados):
    ng = newGuardado(datos.nickname, datos.idP)
    return ng

@app.get("/getComentarios{idP}")
async def e_getComentrios(idP : int):
    gc = getComentario(idP)
    return gc

@app.post("/newComentario")
async def e_newComentario(datos : datosComentario):
    nc = newComentario(datos.idPublicacion, datos.nickname, datos.comentario)
    return nc

#  