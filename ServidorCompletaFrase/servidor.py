import socket

def main():
    host = '0.0.0.0'
    port = 5000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print('Servidor escuchando en el puerto:', port)
    
    # El servidor se queda esperando a QUE SE CONECTE un cliente
    comunicacion, addr = server.accept()
    print('Conexion establecida con:', addr)
    
    conexion_activa = True
    
    # El bucle 'while' debe envolver la ESCUCHA de los mensajes, no solo el print
    while conexion_activa:
        # 1. Recibimos el dato UNA SOLA VEZ y lo guardamos en una variable
        datos_recibidos = comunicacion.recv(1024).decode()
        
        # Convertimos a minúsculas para que dé igual si escriben "HOLA", "hola" o "Hola"
        mensaje = datos_recibidos.lower().strip() # .strip() quita espacios o enter invisibles
        
        print(f"El cliente dice: {mensaje}")
        
        # 2. Evaluamos la variable con ifs
        if mensaje == 'salir':
            print("El cliente solicitó cerrar la conexión.")
            comunicacion.send('Adiós!'.encode())
            conexion_activa = False # Esto romperá el bucle while en la próxima vuelta
            
        elif mensaje == 'hola':
            comunicacion.send('Mundo'.encode())
            
        else:
            comunicacion.send('Prueba a poner Hola o salir'.encode())
            
    # Al salir del bucle while, cerramos el socket de comunicación con este cliente
    comunicacion.close()
    print("Conexión cerrada.")

if __name__ == '__main__':
    main()