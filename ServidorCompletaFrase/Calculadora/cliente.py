import socket

def main():
    host = '127.0.0.1'  # IP local del servidor
    port = 6000       # Puerto corregido
    
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, port))
    print('Has establecido conexión con el servidor de operaciones.\n')
    
    # Capturamos e imprimimos el mensaje de bienvenida inicial del servidor
    bienvenida = cliente.recv(1024).decode()
    print(bienvenida)

    while True:
        # Pedimos los datos al usuario
        datos = input("Ingrese la operacion y sus dijitos separados por ';' (ejemplo: suma;5;3): ")
        datos = datos.lower().strip()
           
        # Enviamos la operación al servidor
        cliente.send(datos.encode())
        
        # Recibimos la respuesta (el resultado + el menú de la siguiente vuelta)
        respuesta = cliente.recv(4096).decode()
        print(respuesta)
        
        # Si el usuario decidió salir, rompemos el bucle del cliente
        if datos.startswith("salir"):
            print("Cerrando la aplicación cliente...")
            break

    # Cerramos el socket al terminar
    cliente.close()

if __name__ == "__main__":
    main()