from request import Request
class Response:
    def __init__(
            self, 
            status_code: int,
            status_message: str,
            headers: dict[str,str],
            version: str = "HTTP/1.1",
            body: bytes = b''):
        self.version = version
        self.status_code = status_code
        self.status_message = status_message
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

