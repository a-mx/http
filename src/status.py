from dataclasses import dataclass
class StatusCodes:
    @dataclass(frozen=True)
    class _Status:
        code: int
        message: str
    OK = _Status(200, "OK")
    CREATED = _Status(201, "Created")
    NO_CONTENT = _Status(204, "No Content")

    MOVED_PERMANENTLY = _Status(301, "Moved Permanently")

    BAD_REQUEST = _Status(400, "Bad Request")
    UNAUTHORIZED = _Status(401, "Unauthorized")
    FORBIDDEN = _Status(403, "Forbidden")
    NOT_FOUND = _Status(404, "Not Found")
    METHOD_NOT_ALLOWED = _Status(405, "Method Not Allowed")

    INTERNAL_SERVER_ERROR = _Status(500, "Internal Server Error")