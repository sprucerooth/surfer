import socket as socket_lib

from http_request import HttpRequest
from http_response import HttpResponse
from exceptions import InvalidHttpRequestException

HOST = ''
PORT = 80
REQ_BUFFER_SIZE = 1024


def start():
    socket_in = _create_socket()

    while True:
        client_socket, client_address = socket_in.accept()
        print(f"Established connection with client: {client_address}")
        print("Waiting for message from client...")

        raw_request = client_socket.recv(REQ_BUFFER_SIZE)
        print(f"Message received. Attempting to parse...")

        try:
            request = HttpRequest(raw_request)
            response = HttpResponse.ok(request)
        except InvalidHttpRequestException as e:
            response = HttpResponse.bad_request(e)

        client_socket.send(response.serialize())
        client_socket.close()
        print("Socket closed.")


def _create_socket():
    socket = socket_lib.socket()
    socket.bind((HOST, PORT))
    socket.listen()
    print(f"Listening on port {PORT}...")
    return socket


if __name__ == '__main__':
    start()
