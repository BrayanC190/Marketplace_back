#  En proceso, no funcional
from conexion import conexion
from fastapi import HTTPException

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
    
#