import socket
def main():
    host = '127.0.0.1' #Ip de dentro de la interfaz de loopback
    port =  5000
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    dominio = input('Ingrese el dominio a resolver: ')
    client.send(dominio.encode())
    respuesta = client.recv(4096).decode()
    print('Respuesta del servidor:', respuesta)
    client.close()
if __name__ == '__main__':
    main()  