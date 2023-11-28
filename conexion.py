import mysql.connector

class conexion:
  @staticmethod
  def getConexion():
    conn = mysql.connector.connect(
    host="tecnm.c1etdihcwq78.us-east-2.rds.amazonaws.com",
    user="admin",
    password="TECNM123",
    database="marketplace")  
    return conn