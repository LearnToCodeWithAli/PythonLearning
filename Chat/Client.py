import socket

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ip = "localhost"
        self.port = 5001

    def connect(self):
        self.s.connect((self.ip, self.port))

    def receive_message(self):
        while True:
            message = self.s.recv(1024).decode()
            print("Received message: ", message)

    def send_message(self):
        while True:
            sending_message = input("Message: ")
            self.s.send(sending_message.encode())
