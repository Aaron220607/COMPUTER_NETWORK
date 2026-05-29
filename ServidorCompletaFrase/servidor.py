import socket
def main():
    host = '0.0.0.0'
    port = 5000
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen()
    conexion = True
    comunicacion,addr =server.accept()
    while  conexion:

        print('Conexion establecida con:', addr)
    if comunicacion.recv(1024).decode().equalsIgnorecase('salir') :
        conexion = False
    comunicacion.close()
    if comunicacion.recv(1024).decode().equalsIgnorecase('Hola') :
        comunicacion.send('Mundo'.encode())
        conexion = False
    else:
        comunicacion.send('Prueba a poner Hola'.encode())
    comunicacion.close()
if __name__ == '__main__':
    main()