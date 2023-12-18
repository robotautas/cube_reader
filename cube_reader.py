from time import sleep
import socket
import sys


class AnalyzerReader:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    def connect(self):
        try:
            server_address = (self.host, self.port)
            self.sock.connect(server_address)
        except:
            print("Cannot connect to Cube, check if software is running")

    def disconnect(self):
        self.sock.close()

    
    def send_message(self, text):
        msg = f'{text}\r\n'
        encoded_msg = bytes(msg, 'ascii')
        self.sock.sendall(encoded_msg)

    
    def get_status(self):
        self.send_message('?STS')
        sleep(0.1)
        while True:
            data = self.sock.recv(4096)
            if not data:
                break
            print(f'Received: {data}')
            return

    def get_status_continuous(self):
        #self.send_message('?STS')
        while True:
            data = self.sock.recv(4096)
            if not data:
                break
            print(f'Received: {data}')
            return

    def get_name(self, position):
        self.send_message(f'?NAM {position}')
        sleep(0.1)
        while True:
            data = self.sock.recv(4096)
            if not data:
                break
            print(f'Received: {data}')
            return
        
    def strt(self):
        self.send_message('STRT')
        sleep(0.1)


    def seqon(self):
        self.send_message('SEQON')
        sleep(0.1)

                
if __name__ == '__main__':
    ar = AnalyzerReader('localhost', 1984)
    ar.connect()
    ar.get_status()
    ar.get_name(1)
    ar.strt()
    ar.seqon()
    while 1:
        ar.get_status_continuous()
        #print('in a loop!')
        sleep(0.1)
    ar.disconnect()
