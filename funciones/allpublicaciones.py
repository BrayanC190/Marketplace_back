from conexion import conexion

def getAllPublicaciones(idPublicacion : str):
    conn = conexion().getConexion()
    cursor = conn.cursor()
    cursor.execute(f"call marketplace.getUser('{idPublicacion}')")
    fila = cursor.fetchone()
    #Se crea la lista de publicaciones que contendra (idPublicacion,fecha, Nombre, Precio, Unidad, Descripcion, Nombres, ApellidoP, nickname, Telefono, Correo, Web, Calle1, Calle2, Lote, Colonia, Municipio, Estado, Pais)
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