from conexion import conexion
from datetime import date, datetime

class usuario:
    #tabla usuario
    id = ''
    password = ''
    nombres = ''
    apellidoP = ''
    apellidoM = ''
    fechaN = ''
    correo  = ''
    telefono = ''
    #tabla ubicacion
    calle1 = ''
    calle2 = ''
    colonia = ''
    lote = ''
    municipio = ''
    estado = ''
    pais = ''

    def __init__(self, nickname):
        self.nickname = nickname
        conn = conexion().getConexion()
        cursor = conn.cursor()
        cursor.execute(f"call marketplace.getUser('{nickname}')")
        fila = cursor.fetchone()
        if fila:
            print("Fila encontrada:", fila)
            self.id = fila[0]
            self.password = fila[3]
            self.nombres = fila[4]
            self.apellidoP = fila[5]
            self.apellidoM = fila[6]
            self.fechaN = fila[7]
            self.correo = fila[8] 
            self.telefono = fila[9]
            #tabla ubicacion
            self.calle1 = fila[11]
            self.calle2 = fila[12]
            self.colonia = fila[13]
            self.lote = fila[14]
            self.municipio = fila[15]
            self.estado = fila[16]
            self.pais = fila[17]
            
        else:
            print(f"No se encontró ninguna fila para el usuario {nickname}.")
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()


    def to_dict(self):
        usuario_dict = {}
        for attr in vars(self):
            valor = getattr(self, attr)
            if isinstance(valor, (datetime, date)):
                usuario_dict[attr] = valor.isoformat()
            else:
                usuario_dict[attr] = valor
        return usuario_dict