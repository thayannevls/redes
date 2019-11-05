from socket import *
from threading import Thread
from queue import Queue

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

def handle_connection(confirmation_signals):
    response, _ = udp_socket.recvfrom(BUFFER_SIZE)
    confirmation_signals.put(response.decode('utf-8'))

if __name__ == '__main__':
    confirmation_signals = Queue() # ACKs
    udp_socket = create_socket()
    message = input('op: ')
    send_message(udp_socket, message)

    connection = Thread(target=handle_connection, args=(confirmation_signals, ))
    connection.start()
    connection.join(timeout=2)

    if(confirmation_signals.qsize()):
        signal = confirmation_signals.get()

        if(signal == 'ACK'):
            result, _ = udp_socket.recvfrom(BUFFER_SIZE)
            print('ACK Client')
            print(result.decode('utf-8'))
            udp_socket.sendto('ACK'.encode('utf-8'), (SERVER_IP, SERVER_PORT))
        else:
            print('What is this?...')
    else:
        print('Transmission failed!')
    udp_socket.close()

