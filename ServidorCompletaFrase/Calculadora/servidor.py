import socket

def menuOperaciones(data, connection):
    data = data.split(";")
    conexion = True
    match data[0]:
        case "suma":
            resultado = int(data[1]) + int(data[2])
            connection.send(f"El resultado de la suma es: {resultado}\n".encode())
        case "resta":
            resultado = int(data[1]) - int(data[2])
            connection.send(f"El resultado de la resta es: {resultado}\n".encode())
        case "multiplicacion":
            resultado = int(data[1]) * int(data[2])
            connection.send(f"El resultado de la multiplicacion es: {resultado}\n".encode())
        case "division":
            try:
                resultado = int(data[1]) / int(data[2])
                connection.send(f"El resultado de la division es: {resultado}\n".encode())
            except ZeroDivisionError:
                connection.send("Error: No se puede dividir por cero\n".encode())
        case "salir":
            connection.send("Cerrando conexion... ¡Adios!\n".encode())
            conexion = False
            connection.close()
        case _:
            connection.send("Operacion no valida\n".encode())
    return conexion

def main():
    host = '0.0.0.0'
    port = 6000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Servidor escuchando en {host}:{port}")
    
    connection, address = server.accept()
    print(f"Conexión establecida desde {address}")
    
    conexion = True
    connection.send("Bienvenido al servidor de operaciones\n".encode())
    
    while conexion:
        # PUNTOS CLAVE CORREGIDOS:
        # 1. Unificamos todo el menú con saltos de línea '\n' en un único string
        # 2. Añadimos un indicador claro '-> ' al final para que simule una terminal limpia
        menu = (
            "\nEscoga la operacion y sus dijitos.\n"
            "Operaciones disponibles: suma, resta, multiplicacion, division.\n"
            "Para salir escriba: salir\n"
            "-> "
        )
        
        # Hacemos UN SOLO send con todo el bloque ordenado
        connection.send(menu.encode())
        
        # El servidor se queda aquí pausado esperando pacientemente
        data = connection.recv(1024).decode().lower()
        
        # CONTROL DE SEGURIDAD: Si el cliente se desconecta abruptamente, rompemos el bucle
        if not data:
            print(f"El cliente {address} se ha desconectado de forma abrupta.")
            break
            
        conexion = menuOperaciones(data, connection)

if __name__ == "__main__":
    main()