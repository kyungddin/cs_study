# TCP Socket Server
from socket import *
serverName = 'kyungddin'
serverPort = 12000

# TCP 소켓 생성
server_socket = socket(AF_INET, SOCK_STREAM)

# 소켓을 포트에 바인딩
server_socket.bind((serverName, serverPort))

# 클라이언트의 연결 요청을 기다림
server_socket.listen(1)
print('The server is ready to receive')

while True:
    # 클라이언트의 연결 요청 수락
    connectionSocket, addr = server_socket.accept()
    print('Connected by', addr)

    # 클라이언트로부터 메시지 받기
    message = connectionSocket.recv(1024).decode()
    print('Received message from client:', message)

    # 메시지를 대문자로 변환
    modifiedMessage = message.upper()

    # 변환된 메시지를 클라이언트로 전송
    connectionSocket.send(modifiedMessage.encode())

    # 연결 소켓 닫기
    connectionSocket.close()