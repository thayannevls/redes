from socket import *
from threading import Thread
from queue import Queue
from time import sleep

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5005
BUFFER_SIZE = 1024

def create_socket():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    return udp_socket

def send_message(udp_socket, message):
    udp_socket.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))

def receive_message(udp_socket):
    response, client = udp_socket.recvfrom(BUFFER_SIZE)
    udp_socket.sendto('ACK'.encode('utf-8'), client)
    return response.decode('utf-8')

def await_confirmation(operation, confirmation_signals):
    send_message(udp_socket, operation)
    response, client = udp_socket.recvfrom(BUFFER_SIZE)
    response = response.decode('utf-8')
    if(response):
        if(response == 'ACK'):
            confirmation_signals.put(response)
        else:
            print('\033[95m' + 'Answer: ' + response + '\033[0m')


if __name__ == '__main__':
    confirmation_signals = Queue() # ACKs
    udp_socket = create_socket()
    operation = input('Operation: ')

    while(True):
        connection = Thread(target=await_confirmation, args=(operation, confirmation_signals, ))
        connection.start()
        connection.join(timeout=2)

        if(confirmation_signals.qsize()):
            break
        print('\033[91m' + 'No response from server. Trying again...' + '\033[0m')

    answer = receive_message(udp_socket)
    if(answer and answer != 'ACK'):
        print('\033[95m' + 'Answer: ' + answer + '\033[0m')

    if(confirmation_signals.qsize()):
        signal = confirmation_signals.get()

        if(signal == 'ACK'):
            print('Client received ACK')
            udp_socket.sendto('ACK'.encode('utf-8'), (SERVER_IP, SERVER_PORT))
        else:
            print('What is this?...')
   
    udp_socket.close()

