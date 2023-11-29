from conexion import conexion

def getAllPublicaciones(idPublicacion: int):
    conn = conexion().getConexion()
    cursor = conn.cursor()
    cursor.execute(f"call marketplace.allPublicacion({idPublicacion})")
    fila = cursor.fetchall()
    if fila:
        publicacion = {
           'idPublicacion' : idPublicacion,
            'fecha' : fila[0][1],
            'nombre' : fila[0][2],
            'precio' : fila[0][3],
            'unidad' : fila[0][4],
            'descripcion' : fila[0][5],
            'nombres' : fila[0][6],
            'apellidoP' : fila[0][7],
            'nickname' : fila[0][8],
            'telefono' : fila[0][9],
            'correo' : fila[0][10],
            'web' : fila[0][11],
            'calle1' : fila[0][12],
            'calle2' : fila[0][13],
            'lote' : fila[0][14],
            'colonia' : fila[0][15],
            'municipio' : fila[0][16],
            'estado' : fila[0][17],
            'pais' : fila[0][18],
        }
        cursor.close()
        conn.close()
        return publicacion
    else:
        cursor.close()
        conn.close()
        return False