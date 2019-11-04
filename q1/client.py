from socket import *

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

def create_socket():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    return udp_socket

def send_message(udp_socket, message):
    udp_socket.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))

def receive_message(udp_socket):
    return udp_socket.recvfrom(BUFFER_SIZE)

if __name__ == '__main__':
    udp_socket = create_socket()
    message = input('Op: ')
    send_message(udp_socket, message)
    print(receive_message(udp_socket)[0].decode('utf-8'))
