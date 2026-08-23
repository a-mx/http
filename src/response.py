from request import Request
class Response:
    STATUS_CODES = {
        200: "OK",
        201: "Created",
        204: "No Content",

        301: "Moved Permanently",

        400: "Bad Request",
        401: "Unauthorized",
        404: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",

        500: "Internal Server Error",
    }
    def __init__(
            self, 
            status_code: int,
            headers: dict[str,str],
            version: str = "HTTP/1.1",
            body: bytes = b''):
        self.version = version
        self.status_code = status_code
        self.status_message = self.STATUS_CODES[self.status_code]
        self.headers = headers
        self.body = body

    def to_bytes(self) -> bytes:
        self.headers["Content-Length"] = str(len(self.body))

        status_line = f"{self.version} {self.status_code} {self.status_message}\r\n"

        headers = "".join(
            f"{name}: {value}\r\n"
            for name, value in self.headers.items()
        )

        return status_line.encode() + headers.encode() + b"\r\n" + self.body
        

