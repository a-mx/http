class Request:
    def __init__(self, unparsed: str):
        self.unparsed = unparsed
        self.method = None
        self.path = None
        self.version = None
        self.headers = {}

        for idx, line in enumerate(self.unparsed.splitlines()):
            if idx == 0: #Request line
                line = line.split()
                self.method = line[0]
                self.path = line[1]
                self.version = line[2]
            elif line == '': #Empty line
                continue
            else: #Request headers
                line = line.split(": ")
                self.headers[line[0]] = line[1]
