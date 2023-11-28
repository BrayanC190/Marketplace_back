from conexion import conexion
import bcrypt

def getUser(nickname : str):
    conn = conexion().getConexion()
    cursor = conn.cursor()
    cursor.execute(f"call marketplace.getUser('{nickname}')")
    fila = cursor.fetchone()
    if fila:
        usuario = {
            'id' : fila[0],
            'nickname' : nickname,
            'password' : fila[3],
            'nombres' : fila[4],
            'apellidoP' : fila[5],
            'apellidoM' : fila[6],
            'fechaN' :  fila[7],
            'correo' : fila[8],
            'telefono' : fila[9],

            'calle1' : fila[11],
            'calle2' : fila[12],
            'colonia' : fila[13],
            'lote' : fila[14],
            'municipio' : fila[15],
            'estado' : fila[16],
            'pais' : fila[17],
        }               
        cursor.close()
        conn.close()
        return usuario 
    else:         
        cursor.close()
        conn.close()
        return False
    
def updateUser(nickname : str, telefono : str, calle1 : str, calle2 : str, colonia : str, lote : int, municipio : str, estado : str, pais : str):
    conn = conexion().getConexion()
    cursor = conn.cursor()
    cursor.execute(f"call updateUser('{nickname}', '{telefono}','{calle1}', '{calle2}', '{colonia}', {lote}, '{municipio}', '{estado}', '{pais}')")
    cursor.close()
    conn.close()

def createUser(nickname : str, password :str, nombres : str, apellidoP : str, apellidoM :str, fechaN : str, correo : str):
    conn = conexion().getConexion()
    cursor = conn.cursor()  
    pass_hash = hash_password(password)
    cursor.execute(f"call newUserBasic('{nickname}', '{pass_hash}', '{nombres}', '{apellidoP}', '{apellidoM}', '{fechaN}', '{correo}')")  
    cursor.close()
    conn.close()

def hash_password(password):
    salt = bcrypt.gensalt()
    pas = bcrypt.hashpw(password.encode('utf-8'), salt)
    return pas.decode('utf-8')