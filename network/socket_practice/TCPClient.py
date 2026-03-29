# TCP Socket Client
from socket import *
serverName = 'kyungddin'
serverPort = 12000

# TCP 소켓 생성
client_socket = socket(AF_INET, SOCK_STREAM)

# 서버에 연결
client_socket.connect((serverName, serverPort))

# 사용자로부터 메시지 입력
message = input('Enter a message to send to the server: ')

# 메시지를 서버로 전송
client_socket.send(message.encode())

# 서버로부터 변환된 메시지 받기
modifiedMessage = client_socket.recv(1024).decode()
print('Message from server:', modifiedMessage)

# 소켓 닫기
client_socket.close()