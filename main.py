import socket as socket_lib
from http_request import *
from exceptions import *

HOST = ''
PORT = 80
REQ_BUFFER_SIZE = 1024


def start():
    socket_in = socket_lib.socket()
    socket_in.bind((HOST, PORT))
    socket_in.listen()

    print(f"Listening on port {PORT} ...")

    while True:
        client_socket, client_address = socket_in.accept()
        client_request = client_socket.recv(REQ_BUFFER_SIZE)

        try:
            request_method, requested_resource = parse(client_request)
        except InvalidHttpRequestException:
            client_socket.send(b'Invalid request!')
            client_socket.close()
            continue

        response = f"OK! Your request was: {request_method} {requested_resource}"
        client_socket.send(response.encode())

        client_socket.close()


if __name__ == '__main__':
    start()
