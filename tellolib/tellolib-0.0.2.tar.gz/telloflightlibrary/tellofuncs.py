import socket

class Tello:
    def __init__(self, port) :
        self.ip = "127.0.0.1"
        self.port = port
        self.addr = (self.ip, self.port)
        self.telloport = 8889
        self.telloip = "192.168.10.1"
        self.telloaddr = (self.telloip, self.telloport)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def sendcommand(self, command):
        try:
            command = command.encode()
            self.sock.sendto(command, self.telloaddr)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
            print('send command')
    def connect(self):
        try:
            print('connect')
            self.sock.bind(self.addr)
            self.sendcommand('command')
        except socket.error as msg:
            print("error sending message " + str(msg))
            print(msg[0])
            print(msg[1])
    def takeoff(self):
        try:
            self.sendcommand('takeoff')
        except socket.error as msg:
            print("error sending message " + str(msg))
    def land(self):
        try:
            self.sendcommand('land')
        except socket.error as msg:
            print("error sending message " + str(msg))
    def forward(self, num):
        try:
            self.sendcommand('forward ' + num)
        except socket.error as msg:
            print("error sending message " + str(msg))
    def backward(self, num):
        try:
            self.sendcommand('back ' + num)
        except socket.error as msg:
            print("error sending message " + str(msg))
    def right(self, num):
        try:
            self.sendcommand('right ' + num)
        except socket.error as msg:
            print("error sending message " + str(msg))
    def left(self, num):
        try:
            self.sendcommand('left ' + num)
        except socket.error as msg:
            print("error sending message " + str(msg))
    def rotatecw(self, degree):
        try:
            self.sendcommand('cw'  + degree)
        except socket.error as msg:
            print("error sending message " + str(msg))
    def rotateccw(self, degree):
        try:
            self.sendcommand('ccw'  + degree)
        except socket.error as msg:
            print("error sending message " + str(msg))

    
    
        
        



