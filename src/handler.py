from request import Request
from status import StatusCodes
from response import Response
from pathlib import Path
class Handler:
    def __init__(self, static_dir: str):
        self.static_dir = Path(static_dir).resolve()

    def handle(self, req: Request) -> Response:
        match req.method:
            case "GET":
                return self.handle_get(req)
                
            case "POST":
                raise Exception("TODO")
            case _:
                return Response(
                    status_code=StatusCodes.METHOD_NOT_ALLOWED.code,
                    status_message=StatusCodes.METHOD_NOT_ALLOWED.message,
                    headers={}
                )

    def handle_get(self, req: Request) -> Response:
        relative_path = "index.html" if req.path == "/" else req.path.lstrip("/")
        path = (self.static_dir / relative_path).resolve()

        if not path.is_relative_to(self.static_dir):
            return self.error_response(StatusCodes.FORBIDDEN)

        if not path.exists() or not path.is_file():
            return self.error_response(StatusCodes.NOT_FOUND)

        body = path.read_bytes()

        return Response(
            status_code=StatusCodes.OK.code,
            status_message=StatusCodes.OK.message,
            headers={"Content-Type": "text/html; charset=utf-8"},
            body=body
        )

    @staticmethod  
    def error_response(status: StatusCodes._Status) -> Response:
        return Response(
            status_code=status.code,
            status_message=status.message,
            headers={}
        )
            