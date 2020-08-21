import socket
from datetime import datetime

host = ''
ip = input("IP de quem quer conversar: ")

myPort = 7000
otherPort = 7001

myAddress = (host, myPort)
otherAddress = (ip, otherPort)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(myAddress)

serverSocket.listen(10)
print('Aguardando conexao com cliente')
connection, cliente = serverSocket.accept()
print('Conectado ao cliente' )

clientName = connection.recv(1024).decode("utf-8")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(otherAddress)

myName = input("Seu nome: ")
clientSocket.send(myName.encode('utf-8'))

while True:
    # receber
    print( "aguardando mensagem..." )
    receive = connection.recv(1024)

    currentyTime = datetime.now().strftime('%H:%M:%S')
    print( clientName + " às " + currentyTime + ": " + receive.decode("utf-8") )

    # enviar
    message = input("Eu: ")
    clientSocket.send(message.encode('utf-8'))

serverSocket.close()
clientSocket.close()