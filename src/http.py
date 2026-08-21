import socket
class HTTP:
    def __init__(self, ip: str, port: int) -> None:
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
    
    def start(self) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
        self.s.bind(self.address)
        self.s.listen()
        print(f"Listening on {self.address}")
        
        while True:
            conn, addr = self.s.accept()
            request = conn.recv(1024).decode()
            print(f"Request:\n{request}")
            conn.close()

def main():
    ip = '0.0.0.0'
    port = 8080
    http = HTTP(ip, port)
    http.start()

if __name__ == "__main__":
    main()