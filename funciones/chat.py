from conexion import conexion
from fastapi import HTTPException
from pydantic import BaseModel

class usuariosChat(BaseModel):
    nickname1 : str
    nickname2 : str

class Chat(BaseModel):
    nickname1 : str
    nickname2 : str
    msg : str

class Conversacion(BaseModel):
    nickname : str

def getChat(nickname1 : str, nickname2 : str):
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()   
        cursor.execute(f"call marketplace.getChat('{nickname1}', '{nickname2}')")

        chat = []

        filas = cursor.fetchall()
        for fila in filas:
            msg = {
                'fecha': fila[1],
                'Emisor' : fila[2],
                'mensaje': fila[4], 
            }
            chat.append(msg)

        cursor.close()
        conn.close()
        return chat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def addChat(nickname1 : str, nickname2 : str, mensaje : str):
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()   
        cursor.callproc("addChat", (nickname1, nickname2, mensaje))
        #cursor.execute(f"call marketplace.addChat('{nickname1}', '{nickname2}', '{mensaje}')")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 

def getConversaciones(nickname : str):
    try:
        conn = conexion().getConexion()
        cursor = conn.cursor()   
        cursor.execute(f"call marketplace.getConversaciones('{nickname}')")

        chat = []

        filas = cursor.fetchall()
        for fila in filas:
            
            msg = {}  

            msg['usuario'] = fila[1] if nickname == fila[0] else fila[0]

            chat.append(msg)

        cursor.close()
        conn.close()
        return chat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
#