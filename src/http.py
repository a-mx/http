import socket
from request import Request
from response import Response
from pathlib import Path
from handler import Handler
class HTTP:
    def __init__(self, ip: str, port: int, static_dir: str, log: bool =True) -> None:
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.log = log
        self.static_dir = static_dir
    
    def start(self) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
        self.s.bind(self.address)
        self.s.listen()
        print(f"Listening on {self.address}")
        
        while True:
            conn, addr = self.s.accept()
            data = conn.recv(1024)
            req = Request.parse(
                addr=addr,
                raw=data
            )

            if self.log: print(req)
             
            handler = Handler(
                static_dir=self.static_dir
            )

            response = handler.handle(req)

            conn.sendall(response.to_bytes())
            conn.close()

def main():

    ip = '0.0.0.0'
    port = 8080
    static_dir = Path("static").resolve()

    http = HTTP(
        ip=ip,
        port=port,
        static_dir=static_dir
    )
    
    http.start()

if __name__ == "__main__":
    main()