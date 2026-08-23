import datetime
class Request:
    def __init__(
        self,
        addr : str,
        method : str,
        path : str,
        version : str,
        headers : dict[str, str],
        body : str
    ):  
        self.addr = addr
        self.method = method
        self.path = path
        self.version = version
        self.headers = headers
        self.body = body

    @classmethod
    def parse(cls, addr: str, raw: bytes):

        headers = {}
        body = ""
        for idx, line in enumerate(raw.decode().splitlines()):
            if idx == 0: #Request line
                line = line.split()
                method = line[0]
                path = line[1]
                version = line[2]
            elif line == '': #Empty line
                continue
            else: #Request headers
                line = line.split(": ")
                headers[line[0]] = line[1]
        
        return cls(
            addr=addr,
            method=method,
            path=path,
            version=version,
            headers=headers,
            body=body
        )
    
    def __str__(self) -> str:
        date = datetime.datetime.now()
        return f"[{date}] Request from {self.addr}: {self.method} {self.path} {self.version}"
        
        
