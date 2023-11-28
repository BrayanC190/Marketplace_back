from conexion import conexion

def upload(nickname):
        nickname = nickname
        conn = conexion().getConexion()
        cursor = conn.cursor()
        cursor.execute(f"call marketplace.getUser('{nickname}')")
        fila = cursor.fetchone()
        if fila:
            print("Fila encontrada:", fila)
            id = fila[0]
            password = fila[3]
            nombres = fila[4]
            apellidoP = fila[5]
            apellidoM = fila[6]
            fechaN = fila[7]
            correo = fila[8] 
            telefono = fila[9]
            #tabla ubicacion
            calle1 = fila[11]
            calle2 = fila[12]
            colonia = fila[13]
            lote = fila[14]
            municipio = fila[15]
            estado = fila[16]
            pais = fila[17]
            
        else:
            print(f"No se encontró ninguna fila para el usuario {nickname}.")
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()