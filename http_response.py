from http_request import HttpRequest


class HttpResponse:
    codes: dict = {200: "OK", 400: "Bad request", 401: "Unauthorized", 404: "Not found", 500: "Internal server error"}

    def __init__(self, code, body=''):
        self.code: int = code
        self.body: str = body

    def serialize(self):
        return f"HTTP/1.1 {self.code} {HttpResponse.codes.get(self.code)}\r\n\r\n{self.body}".encode()

    @classmethod
    def bad_request(cls, e: Exception):
        return cls(400)

    @classmethod
    def ok(cls, request: HttpRequest):
        return cls(200, open(request.resource).read())
