import socket

def main():
    host = '0.0.0.0'
    port = 5000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"Servidor escuchando en {host}:{port}")
    
    connection, address = server.accept()
    print(f"Conexión establecida desde {address}")
    
    # BIENVENIDA: Se envía una sola vez al conectar
    connection.send("Bienvenido al servidor de operaciones virtuales.".encode())
    
    conexion = True
    while conexion:
        try:
            # El servidor se queda esperando los datos del cliente
            data = connection.recv(1024).decode().lower()
            
            # Si el cliente se desconecta o escribe 'salir'
            if not data or data == 'salir':
                print(f"Cliente {address} desconectado.")
                conexion = False
                break
                
            menuOperaciones(data, connection)
            
        except ConnectionResetError:
            print(f"El cliente {address} cerró la conexión abruptamente.")
            break
            
    connection.close()
    server.close()

def menuOperaciones(data, connection):
    try:
        data = data.split(";")
        match data[0]:
            case "suma":
                resultado = int(data[1]) + int(data[2])
                connection.send(f"El resultado de la suma es: {resultado}".encode())

            case "resta":
                resultado = int(data[1]) - int(data[2])
                connection.send(f"El resultado de la resta es: {resultado}".encode())

            case "multiplicacion":
                resultado = int(data[1]) * int(data[2])
                connection.send(f"El resultado de la multiplicacion es: {resultado}".encode())
                
            case "division":
                try:
                    resultado = int(data[1]) / int(data[2])
                    connection.send(f"El resultado de la division es: {resultado}".encode())
                except ZeroDivisionError:
                    connection.send("Error: No se puede dividir por cero".encode())
                
            case _:
                connection.send("Error: Operación no reconocida".encode())
                
    except IndexError:
        connection.send("Error: Formato incorrecto. Recuerda usar 'operacion;num1;num2'".encode())

if __name__ == "__main__":
    main()
