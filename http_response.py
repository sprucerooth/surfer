class HttpResponse:
    codes: dict = {200: "OK", 400: "Bad request", 401: "Unauthorized", 404: "Not found", 500: "Internal server error"}

    def __init__(self):
        self.code: int = 0
