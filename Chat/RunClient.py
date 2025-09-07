from Client import Client
import threading

client = Client()
client.connect()

threading.Thread(target=client.receive_message).start()
threading.Thread(target=client.send_message).start()