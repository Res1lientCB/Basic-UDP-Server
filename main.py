import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = ":)"
bytesToSend         = str.encode(msgFromServer)

# Criado socket unidade de transferência básica.

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Vincular ao endereço IP do servidor.

UDPServerSocket.bind((localIP, localPort))

print("Servidor UDP está funcionando corretamente!")

# Lista de unidade de transferência(datagram).

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    
    clientMsg = "Mensagem do Cliente:{}".format(message)
    clientIP  = "Endereço IP do Cliente:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

    # Enviando uma resposta ao cliente.

    UDPServerSocket.sendto(bytesToSend, address)