import socket
from time import sleep
from threading import Thread, Event

HOST = '0.0.0.0'
PORT = 9999

# A is the sender, B is the receiver
ch = 'A'
msg = "Empty Message!"
event = Event()

def main():
    global ch
    
    server = Server().create_server()
    
    print("[*] Waiting For Connection...")
    
    for _ in range(2):
        Thread(target=Request(server).accept, args=(ch, )).start()
        ch = 'B'
            
def handler(client, ch):
    global msg
    
    while True:
        if ch == 'A':
            while True:
                client.send(b"Send To B: ")
                        
                msg = client.recv(1024)
                buf = str(msg.decode()).strip()
                
                # Send to Client B
                event.set()
                print(buf) #? Should send to the other running thread (User B)
                
        elif ch == 'B':
            while True:
                Server().send_to_client_B(client)
    
class Server:  
    def create_server(self) -> socket.socket:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(5)
        socket.setdefaulttimeout(60 * 2)
        
        return server
    
    def send_to_client_B(self, client):
        while event.is_set() != True:
            pass
        client.send(msg)
        event.clear()

class Request:
    def __init__(self, server):
        self.client, self.address = server.accept()
    
    def accept(self, ch):
            print(f"Got Connection From [Client {ch}]:{(self.address)}")
            self.client.send(f"You Are User {ch}.\n".encode())
            
            handler(self.client, ch)
                    
    def decline(self):
        pass

if __name__ == '__main__': main()