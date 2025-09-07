from Server import Server
import threading

server = Server()
threading.Thread(target=server.accept).start()
threading.Thread(target=server.chat).start()


