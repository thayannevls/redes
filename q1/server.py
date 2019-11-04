from socket import *

BUFFER_SIZE = 1024

def start_server(ip, port):
    udp_socket = socket(AF_INET, # Internet
                         SOCK_DGRAM) # UDP
    udp_socket.bind((ip, port))
    
    print('Server is running')
    return(udp_socket)

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
        data, client = udp_socket.recvfrom(BUFFER_SIZE) # buffer size is 1024 bytes
        print('Received message: ', data, 'from ', client)
        response = calculate(data.decode('utf-8'))
        udp_socket.sendto(str(response).encode('utf-8'), client)
