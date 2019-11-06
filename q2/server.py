from socket import *
from threading import Thread
from queue import Queue
from time import sleep

BUFFER_SIZE = 1024

def calculate(message):
    op, a, b = message.split()
    a = int(a)
    b = int(b)

    if(op.upper() == 'ADD'):
        return a + b
    
    elif(op.upper() == 'SUB'):
        return a - b
    
    elif(op.upper() == 'MULT'):
        return a * b

    elif(op.upper() == 'DIV'):
        if(b != 0):
            return a / b
        return 'Denominator cannot be zero'
    elif(op.upper() == 'EXP'):
        return a ** b
    return 'Invalid operation. The options are: ADD, SUB, MULT, DIV and EXP'

def start_server(ip, port):
    udp_socket = socket(AF_INET, # Internet
                         SOCK_DGRAM) # UDP
    udp_socket.bind((ip, port))
    
    print('Server is running')
    return(udp_socket)

def handle_connection(confirmation_signals):
    data, client = udp_socket.recvfrom(BUFFER_SIZE)
    print('Received message: "', data.decode('utf-8'), '" from ', client)
    # sleep(3)
    if(data.decode('utf-8') == 'ACK'):
        confirmation_signals.put(data.decode('utf-8'))
    else:
        response = calculate(data.decode('utf-8'))
        udp_socket.sendto('ACK'.encode('utf-8'), client)
        udp_socket.sendto(str(response).encode('utf-8'), client)

if __name__ == '__main__':
    udp_socket = start_server('127.0.0.1', 5005)
    confirmation_signals = Queue()
    while True:
        connection = Thread(target=handle_connection, args=(confirmation_signals, ))
        connection.start()
        connection.join(timeout=1)

    udp_socket.close()


        
