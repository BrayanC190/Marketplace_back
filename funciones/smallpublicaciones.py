#  En proceso, no funcional
from conexion import conexion
import json

def getSmallPublicaciones():
    conn = conexion().getConexion()
    cursor = conn.curor()
    cursor.execute(f"call marketplace.smallPublicacion()")
    fila = cursor.fetchall()
    #Se crea la lista de publicaciones que contendra (idPublicacion,fecha,Nombre,Precio,Municipio,Estado,Pais)
    publicaciones = []
    for i in range(len(fila)):
        publicaciones.append({
            'idPublicacion' : fila[i][0],
            'fecha' : fila[i][1],
            'nombre' : fila[i][2],
            'precio' : fila[i][3],
            'municipio' : fila[i][4],
            'estado' : fila[i][5],
            'pais' : fila[i][6]
        })
    cursor.close()
    conn.close()
    return publicaciones