import socket
from datetime import datetime

host = ''
ip = input("IP de quem quer conversar: ")

myPort = 7001
otherPort = 7000

myAddress = (host, myPort)
otherAddress = (ip, otherPort)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serverSocket.bind(myAddress)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(otherAddress)

myName = input("Seu nome: ")
clientSocket.send(myName.encode('utf-8'))

serverSocket.listen(10)
print('Aguardando conexao com servidor')
connection, cliente = serverSocket.accept()
print('Conectado ao servidor' )

clientName = connection.recv(1024).decode("utf-8")

while True:
    # enviar
    message = input("Eu: ")
    clientSocket.send(message.encode('utf-8'))

    # receber
    print( "aguardando mensagem..." )
    receive = connection.recv(1024)

    currentyTime = datetime.now().strftime('%H:%M:%S')
    print( clientName + " às " + currentyTime + ": " + receive.decode("utf-8") )

serverSocket.close()
clientSocket.close()