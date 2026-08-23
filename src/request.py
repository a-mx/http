class Request:
    def __init__(
        self,
        method : str,
        path : str,
        version : str,
        headers : dict[str, str],
        body : str
    ):
        self.method = method
        self.path = path
        self.version = version
        self.headers = headers
        self.body = body

    @classmethod
    def parse(cls, raw: bytes):
        print()
        headers = {}
        body = ""
        for idx, line in enumerate(raw.splitlines()):
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
            method=method,
            path=path,
            version=version,
            headers=headers,
            body=body
        )
