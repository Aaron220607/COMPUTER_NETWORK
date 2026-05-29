import socket
def main():
    host = '0.0.0.0'
    port = 5000
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen()
    print('Servidor escuchando en el puerto:',port)
    while True:
        conn, addr = server.accept()
        print('Conexión establecida desde:', addr)
        dominio = conn.recv(1024).decode()
        print('Dominio recibido:', dominio)
        try:
            ip = socket.gethostbyname(dominio)
            ip_servidor = socket.gethostbyname(socket.gethostname())
            respuesta = f"""
            Dominio: {dominio}
            IP del dominio: {ip}
            Tu IP: {addr[0]}
            IP del servidor: {ip_servidor}
            """
        except :
            respuesta = 'Error: No se pudo resolver el dominio.'
            conn.send(respuesta.encode())
            conn.close()