from exceptions import *
from os import path
from http_method import HttpMethod

RES_LOCATION = "res"


class HttpRequest:
    def __init__(self, raw_request: bytes):
        decoded_lines = raw_request.decode("unicode_escape", "utf-8").splitlines()
        self.method, self.resource, self.version = HttpRequest.__parse_start_line(decoded_lines[0])

    @staticmethod
    def __parse_start_line(line: str):
        method, resource, version = HttpRequest.__val_start_line_length(line)
        HttpRequest.__val_method(method)
        resource = HttpRequest.__val_resource(resource)
        HttpRequest.__val_version(version)
        return method, resource, version

    @staticmethod
    def __val_start_line_length(line: str):
        split_line = line.split()
        if not len(split_line) == 3:
            raise InvalidHttpRequestException
        return split_line[0], split_line[1], split_line[2]

    @staticmethod
    def __val_method(method: str):
        if method not in HttpMethod.__members__:
            raise InvalidHttpRequestException
        return HttpMethod[method]

    @staticmethod
    def __val_resource(resource: str):
        if resource == '/':
            resource = 'index.html'
        if not path.exists(f"{RES_LOCATION}/{resource}"):
            raise InvalidHttpRequestException
        return f"{RES_LOCATION}/{resource}"

    @staticmethod
    def __val_version(ver: str):
        if not ver == "HTTP/1.1":
            raise InvalidHttpRequestException
