import socket
from request import Request
from response import Response
class HTTP:
    def __init__(self, ip: str, port: int, log: bool =True) -> None:
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.log = log
    
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

            response = Response(
                status_code=200,
                headers={
                    "Content-Type": "text/html; charset=utf-8",
                },
                body=b'Hello world',
            )
            conn.sendall(response.to_bytes())
            conn.close()

def main():
    ip = '0.0.0.0'
    port = 8080
    http = HTTP(ip, port)
    http.start()

if __name__ == "__main__":
    main()