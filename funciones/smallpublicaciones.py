from conexion import conexion
import json

def getSmallPublicaciones():
    conn = conexion().getConexion()
    cursor = conn.curor()
    cursor.execute(f"call marketplace.smallPublicacion()")
    fila = cursor.fetchone()
    if fila:
        smallPublicacion ={ 
            'idPublicacion': fila[0],
            'fecha': fila[1],
            'Nombre': fila[2],
            'Precio': fila[3],
            'Municipio': fila[4],
            'Estado': fila[5],
            'Pais': fila[6],
        }
        cursor.close()
        conn.close()
        return smallPublicacion 
    else:         
        cursor.close()
        conn.close()
        return False