from exceptions import *

METHODS = ('HEAD', 'GET', 'POST', 'PUT')


def parse(http_request: bytes):
    decoded_request = http_request.decode("unicode_escape", "utf-8")
    request_method, requested_resource = _split_request(decoded_request)

    if request_method not in METHODS:
        raise InvalidHttpRequestException

    return request_method, requested_resource


def _split_request(request: str):
    split_request = request.split(' ', 2)
    if len(split_request) < 2:
        raise InvalidHttpRequestException
    else:
        return split_request[0], split_request[1]
