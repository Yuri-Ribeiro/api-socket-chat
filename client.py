import socket

ip = input('digite o ip de conexao: ')
port = 7000
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)
mensagem = input("digite uma mensagem para enviar ao servidor")
client_socket.send(mensagem.encode('utf-8'))
print('mensagem enviada')
client_socket.close()