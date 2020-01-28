import socket as socket_lib
from http_request import *
from exceptions import *

HOST = ''
PORT = 80
REQ_BUFFER_SIZE = 1024

socket_in = socket_lib.socket()
socket_in.bind((HOST, PORT))
socket_in.listen()

print(f"Listening on port {PORT} ...")

while True:
    client_socket, client_address = socket_in.accept()
    client_request = client_socket.recv(REQ_BUFFER_SIZE)

    try:
        request_method, request_resource = parse(client_request)
    except InvalidHttpRequestException:
        client_socket.send(b'Invalid request!')
        client_socket.close()
        continue

    client_socket.send(b'OK!')

    client_socket.close()
