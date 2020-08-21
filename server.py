import socket
from datetime import datetime

host = ''
myPort = 7000

myAddress = (host, myPort)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(myAddress)

serverSocket.listen(10)
print('Aguardando conexao com cliente')
connection, cliente = serverSocket.accept()
print('Conectado ao cliente' )

otherIP = input("IP de quem quer conversar: ")
otherPort = 7001
otherAddress = (otherIP, otherPort)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(otherAddress)


myName = input("Seu nome: ")
clientSocket.send(myName.encode('utf-8'))

print("Aguardando outra pessoa informar nome...")
clientName = connection.recv(1024).decode("utf-8")

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