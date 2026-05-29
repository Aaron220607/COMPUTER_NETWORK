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
    conexion = True
    while conexion:
        connection.send("Bienvenido al servidor".encode())
        connection.send("Escoga la operacion y sus dijitos".encode())
        data = connection.recv(1024).decode().lower()
        menuOperaciones(data, connection)


def menuOperaciones(data, connection):
    data = data.split(";")
    match data[0]:
        case "suma":
            resultado = int(data[1]) + int(data[2])
            connection.send(f"El resultado de la suma es: {resultado}".encode())

        case "resta":
            resultado = int(data[1]) - int(data[2])
            connection.send(f"El resultado de la resta es: {resultado}".encode())

        case _:
            connection.send("Operación no reconocida".encode())
    