from datetime import datetime

# Función para convertir fecha de DD/MM/AAAA a AAAA-MM-DD
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

# Ejemplo de uso
fecha_dd_mm_aaaa = "31/12/2023"
fecha_aaaa_mm_dd = convertir_fecha(fecha_dd_mm_aaaa)
print(fecha_aaaa_mm_dd)



