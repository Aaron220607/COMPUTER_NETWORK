import socket 
def main():
    host = '127.0.0.1'
    port = 5000
    cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cliente.connect((host, port))
    print(cliente.recv(1024).decode())
    inpuOperacion = input("Ingrese la operacion y sus dijitos separados por ';' (ejemplo: suma;5;3): ")
    cliente.send(inpuOperacion(4096).encode())
    print(cliente.recv(1024).decode())
if __name__ == "__main__":
    main()