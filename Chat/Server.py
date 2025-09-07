import socket
import threading

class Server:
    def __init__(self):
        self.port = 5001
        self.clients = []
        self.ip = "localhost"
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ip, self.port))
        self.s.listen()
        self.s.setblocking(False)

    def accept(self):
        while True:
            try:
                c,addr = self.s.accept()
                self.clients.append(c)
                print(f"Connection from {addr} accepted")
            except:
                continue

    def broadcast(self, message):
        for c in self.clients:
            try:
                c.send(message.encode())
            except:
                current_client = self.clients.pop(c)
                print(f"Connection from {current_client} lost")
                continue

    def chat(self):
        while True:
            if len(self.clients) > 0:
                for c in self.clients:
                    try:
                        message = c.recv(self.port).decode()
                        if message:
                            print(message)
                            self.broadcast(message)
                    except:
                        continue

