import socket as socket_lib

from http_request import *
from http_response import HttpResponse

HOST = ''
PORT = 80
REQ_BUFFER_SIZE = 1024


def start():
    socket_in = _create_socket()

    while True:
        client_socket, client_address = socket_in.accept()
        print(f"Established connection with client: {client_address}")
        print("Waiting for message from client...")

        client_request = client_socket.recv(REQ_BUFFER_SIZE)
        print(f"Message received. Attempting to parse...")

        response = HttpResponse()
        try:
            request_method, requested_resource = parse(client_request)
            response.code = 200
        except InvalidHttpRequestException as e:
            response.code = 400

        client_socket.send(_serialize_response(response))
        client_socket.close()
        print("Socket closed.")


def _create_socket():
    socket = socket_lib.socket()
    socket.bind((HOST, PORT))
    socket.listen()
    print(f"Listening on port {PORT}...")
    return socket


def _serialize_response(resp: HttpResponse):
    return f"{resp.code} {HttpResponse.codes.get(resp.code)}\n".encode()


if __name__ == '__main__':
    start()
