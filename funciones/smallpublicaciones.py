#  En proceso, no funcional
from conexion import conexion
from pydantic import BaseModel
from fastapi import HTTPException

class smallpublicacion(BaseModel):
    id : int
    fecha : str
    Nombre : str
    Precio : str
    Municipio : str
    Estado : str
    Pais : str

''''
def getSmallPublicaciones():
    try:
        conn = conexion().getConexion()
        cursor = conn.curor()
        cursor.execute(f"call marketplace.smallPublicacion()")
        fila = cursor.fetchone()
        if fila:
            usuario = {
                'id' : fila[0],
                'fecha' : nickname,
                'Nombre' : fila[3],
                'Precio' : fila[4],
                'Municipio' : fila[5],
                'Estado' : fila[6],
                'Pais' :  fila[7],
            }               
            cursor.close()
            conn.close()        
            return usuario 
        else:         
            cursor.close()
            conn.close()
            return False
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    '''
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
