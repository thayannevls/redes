from socket import *
from threading import Thread
from queue import Queue

BUFFER_SIZE = 1024

def start_server(ip, port):
    udp_socket = socket(AF_INET, # Internet
                         SOCK_DGRAM) # UDP
    udp_socket.bind((ip, port))
    
    print('Server is running')
    return(udp_socket)

def handle_connection():
    data, client = udp_socket.recvfrom(BUFFER_SIZE)
    print('Received message: ', data, 'from ', client)
    if(data.decode('utf-8') == 'ACK'):
        return
    
    response = calculate(data.decode('utf-8'))

    udp_socket.sendto('ACK'.encode('utf-8'), client)
    udp_socket.sendto(str(response).encode('utf-8'), client)

    response, _ = udp_socket.recvfrom(BUFFER_SIZE)
    confirmation_signals.put(response.decode('utf-8'))

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

if __name__ == '__main__':
    udp_socket = start_server('127.0.0.1', 5005)
    while True:
        confirmation_signals = Queue()
        connection = Thread(target=handle_connection)
        connection.start()
        connection.join(timeout=1)

        if(confirmation_signals.qsize()):
            signal = confirmation_signals.get()

            if(signal == 'ACK'):
                result, _ = udp_socket.recvfrom(BUFFER_SIZE)
                print('ACK Server')
                print(result.decode('utf-8'))
                udp_socket.sendto('ACK'.encode('utf-8'), (SERVER_IP, SERVER_PORT))
            else:
                print('What is this?...')
    udp_socket.close()


        
