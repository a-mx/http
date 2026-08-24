from request import Request
from status import StatusCodes
from response import Response
from pathlib import Path
class Handler:
    def __init__(self, static_dir: str):
        self.static_dir = static_dir

    def handle(self, req: Request):
        match req.method:
            case "GET":
                path = (self.static_dir / req.path.lstrip("/")).resolve()

                if not path.is_relative_to(self.static_dir):
                    status = StatusCodes.FORBIDDEN
                    return Response(
                        status_code=status.code,
                        status_message=status.message,
                        headers={}
                    )
                
                if req.path == "/":
                    path = self.static_dir / "index.html"
                else:
                    path = self.static_dir / req.path.lstrip("/")

                if not path.exists():
                    status = StatusCodes.NOT_FOUND
                    return Response(
                        status_code=status.code,
                        status_message=status.message,
                        headers={}
                    )
                    
                if not path.is_file():
                    status = StatusCodes.NOT_FOUND
                    return Response(
                        status_code=status.code,
                        status_message=status.message,
                        headers={}
                    )
                status = StatusCodes.OK
                with open(path, "r") as f:
                    body = f.read()
            
                return Response(
                    status_code=status.code,
                    status_message=status.message,
                    headers={"Content-Type": "text/html; charset=utf-8"},
                    body=body.encode(encoding='utf-8')
                )
                
            case "POST":
                raise Exception("TODO")
            case _:
                pass
        