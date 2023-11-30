from conexion import conexion
import bcrypt
from pydantic import BaseModel
from datetime import datetime
from fastapi import HTTPException

class credenciales(BaseModel):
    nickname: str
    password: str

class updateDatos(BaseModel):
    nickname : str
    telefono : str
    calle1 : str
    calle2 : str
    colonia : str
    lote : int
    municipio : str
    estado : str
    pais : str

class newDatos(BaseModel):
    nickname : str
    password :str
    nombres : str
    apellidoP : str
    apellidoM :str
    fechaN : str
    correo : str

def validateLogin(nickname : str, password : str):
    conn = conexion().getConexion()
    cursor = conn.cursor()
    cursor.execute(f"SELECT pass FROM usuarios WHERE nickname = '{nickname}'")
    fila = cursor.fetchone()
    pBD = fila[0]
    password_BD = pBD.encode('utf-8')

    password_hash = hash_password(password)

    is_correct = verify_password(password_BD, password)

    return is_correct

    ##return {"bd": password_BD, "pass":password_hash, "is":is_correct}

def getUser(nickname : str):
    print(f"call marketplace.getUser('{nickname}')")
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()
        cursor.execute(f"call marketplace.getUser('{nickname}')")
        #numero_de_filas = len(cursor)        
        fila = cursor.fetchone()
        print(len(fila))
        if(fila):

            usuario = {
                    'id' : fila[0],
                    'nickname' : nickname,
                    'password' : fila[3],
                    'nombres' : fila[4],
                    'apellidoP' : fila[5],
                    'apellidoM' : fila[6],
                    'fechaN' :  fila[7],
                    'correo' : fila[8],
                    'telefono' : fila[9]
                }

            if len(fila) >= 11:                

                    usuario['calle1'] = fila[11]
                    usuario['calle2'] = fila[12]
                    usuario['colonia'] = fila[13]
                    usuario['lote'] = fila[14]
                    usuario['municipio'] = fila[15]
                    usuario['estado'] = fila[16]
                    usuario['pais'] = fila[17]
                              
            cursor.close()
            conn.close()        
            return usuario 
        else:         
            cursor.close()
            conn.close()
            return False        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def updateUser(nickname : str, telefono : str, calle1 : str, calle2 : str, colonia : str, lote : int, municipio : str, estado : str, pais : str):
    conn = conexion().getConexion()
    cursor = conn.cursor()
    cursor.execute(f"call updateUser('{nickname}', '{telefono}','{calle1}', '{calle2}', '{colonia}', {lote}, '{municipio}', '{estado}', '{pais}')")
    cursor.close()
    conn.close()

def createUser(nickname : str, password :str, nombres : str, apellidoP : str, apellidoM :str, fechaN : str, correo : str):
    conn = conexion().getConexion()
    cursor = conn.cursor()  
    pass_hash = hash_password_str(password)
    fecha = convertir_fecha(fechaN)
    cursor.execute(f"call newUserBasic('{nickname}', '{pass_hash}', '{nombres}', '{apellidoP}', '{apellidoM}', '{fecha}', '{correo}')")  
    cursor.close()
    conn.close()

#funciones propias
def hash_password_str(password):
    salt = bcrypt.gensalt()
    pas = bcrypt.hashpw(password.encode('utf-8'), salt)
    return pas.decode('utf-8')

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def verify_password(stored_hash, user_input_password):
    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode('utf-8')

    return bcrypt.checkpw(user_input_password.encode('utf-8'), stored_hash)

def convertir_fecha(fecha_dd_mm_aaaa):
    try:
        # Parsea la fecha en formato DD/MM/AAAA
        fecha_obj = datetime.strptime(fecha_dd_mm_aaaa, '%d/%m/%Y')
        
        # Convierte la fecha al formato AAAA-MM-DD
        fecha_aaaa_mm_dd = fecha_obj.strftime('%Y-%m-%d')
        
        return fecha_aaaa_mm_dd
    except ValueError:
        # Maneja errores si la fecha no es válida
        return "Fecha inválida"