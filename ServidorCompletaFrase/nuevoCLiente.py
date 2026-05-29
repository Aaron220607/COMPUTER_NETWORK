import socket

def main():
    host = '127.0.0.1'  # Ip de dentro de la interfaz de loopback
    port = 5000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print('Has establecido conexion con el servidor')

    while True:
        print('Escribe el numero de la opcion que deseas realizar')
        print('1. Salir')
        print('2. Completar frase')
        try:
            opcion = int(input('Opcion: '))
        except ValueError:
            print('Opcion no valida, por favor ingresa un numero')
            continue

        match opcion:
            case 1:
                client.send('salir'.encode())
                print('Cerrando conexion...')
                break
            case 2:
                frase = input('Ponga hola y el servidor le respondera con mundo: ')
                client.send(frase.encode())
                respuesta = client.recv(4096).decode()
                print('Respuesta del servidor:', respuesta)
            case _:
                print('Opcion no valida, por favor ingresa una opcion valida')
                

    client.close()

if __name__ == '__main__':
    main()
    