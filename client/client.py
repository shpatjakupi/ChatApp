from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread, Lock
import time

class Client:

    HOST = 'localhost'
    PORT = 5500
    ADDR = (HOST,PORT)
    BUFSIZ = 512


    def __init__(self, name):

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages = []
        receive_thread = Thread(target=self.recieve_messages)
        receive_thread.start()
        self.send_message(name)
        self.lock = Lock()

    def recieve_messages(self):
    
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode()
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
            except Exception as e:
                print("[EXCEPTION]", e)
                break
            
    def send_message(self, msg):

        try:
            self.client_socket.send(bytes(msg,"utf8"))
            if msg == "{quit}":
                self.client_socket.close()
        except Exception as e:
            self.client_socket = socket(AF_INET, SOCK_STREAM)
            self.client_socket.connect(self.ADDR)
            print(e)
            
    def get_messages(self):

        messages_copy = self.messages[:]
        self.lock.acquire()
        self.messages = []
        self.lock.release()
        
        return messages_copy
    
    def disconnect(self):
        self.send_message("{quit}")