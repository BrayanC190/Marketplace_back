#  En proceso, no funcional
from conexion import conexion
from fastapi import HTTPException
from pydantic import BaseModel

class datosComentario(BaseModel):
    idPublicacion : int
    nickname : str
    comentario : str

class datosGuardados(BaseModel):
    nickname : str
    idP : int

class Publicacion(BaseModel):
    nickname : str 
    nombre: str
    precio: str
    unidad: str
    descripcion: str
    telefono: str
    correo: str
    web: str
    calle1: str 
    cale2 : str
    colonia: str
    lote: int
    municipio : str
    estado: str
    pais: str


def getSmallPublicaciones():
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()  # Asegúrate de que sea 'cursor', no 'curor'
        cursor.execute("call marketplace.smallPublicacion()")

        # Inicializa una lista vacía para almacenar todos los usuarios
        usuarios = []

        # Usa fetchall() para obtener todas las filas
        filas = cursor.fetchall()
        for fila in filas:
            usuario = {
                'id': fila[0],
                'fecha': fila[1],  # Asegúrate de que 'fecha' esté asignada correctamente
                'Nombre': fila[2],
                'Precio': fila[3],
                'Municipio': fila[4],
                'Estado': fila[5],
                'Pais': fila[6],
            }
            usuarios.append(usuario)

        cursor.close()
        conn.close()
        return usuarios  # Devuelve la lista de usuarios

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getAllPublicaciones(idPublicacion: int):
    conn = conexion().getConexion()
    cursor = conn.cursor()
    cursor.execute(f"call marketplace.allPublicacion({idPublicacion})")
    fila = cursor.fetchone()
    if fila:
        publicacion = {
           'idPublicacion' : idPublicacion,
            'fecha' : fila[1],
            'nombre' : fila[2],
            'precio' : fila[3],
            'unidad' : fila[4],
            'descripcion' : fila[5],
            'nombres' : fila[6],
            'apellidoP' : fila[7],
            'nickname' : fila[8],
            'telefono' : fila[9],
            'correo' : fila[10],
            'web' : fila[11],
            'calle1' : fila[12],
            'calle2' : fila[13],
            'lote' : fila[14],
            'colonia' : fila[15],
            'municipio' : fila[16],
            'estado' : fila[17],
            'pais' : fila[18],
        }
        cursor.close()
        conn.close()
        return publicacion
    else:
        cursor.close()
        conn.close()
        return False

def newPost(nickname, nombre, precio, unidad, descripcion, telefono, correo, web, c1, c2, c, l, m, e, p): 
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()   
        cursor.callproc("newPublicacion", (nickname, nombre, precio, unidad, descripcion, telefono, correo, web, c1, c2, c, l, m, e, p, '@p_referenciaOut'))
        cursor.execute("SELECT @p_referenciaOut")
        fila = cursor.fetchone()
        cursor.close()
        conn.close()
        return fila[0]
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))

def getGuardados(nickname : str):
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()  
        cursor.execute(f"call marketplace.getGuardados('{nickname}')")

        guardados = []

        filas = cursor.fetchall()
        for fila in filas:
            publicacion = {
                'id': fila[0],
                'idPublicacion' : fila[1],
                'fecha': fila[2], 
                'Nombre': fila[3],
                'Precio': fila[4],
                'Municipio': fila[5],
                'Estado': fila[6],
                'Pais': fila[7],
            }
            guardados.append(publicacion)

        cursor.close()
        conn.close()
        return guardados

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def newGuardado(nickname : str, idP : int):
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()   
        cursor.callproc("newGuardado", (nickname, idP))
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def getComentario(idP : int):
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()   
        cursor.execute(f"call marketplace.getComentario({idP})")

        guardados = []

        filas = cursor.fetchall()
        for fila in filas:
            publicacion = {
                'idComentario': fila[0],
                'idPublicacion' : fila[1],
                'fechaPublicacion': fila[2], 
                'nickname': fila[3],
                'comentario': fila[4],
            }
            guardados.append(publicacion)

        cursor.close()
        conn.close()
        return guardados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def newComentario(idP : int, nickname : str, comentario : str):
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()   
        cursor.callproc("newComentario", (idP, nickname, comentario))
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def misPost(nickname : str):
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()   
        cursor.execute(f"call marketplace.misPost('{nickname}')")

        guardados = []

        filas = cursor.fetchall()
        for fila in filas:
            publicacion = {
                'idPublicacion' : fila[0],
                'fechaPublicacion': fila[1],
                'nombrePublicacion' : fila[2],
                'precio' : fila[3],
                'municipio' : fila[4],
                'estado' : fila[5],
                'pais' : fila[6],
            }
            guardados.append(publicacion)

        cursor.close()
        conn.close()
        return guardados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#
