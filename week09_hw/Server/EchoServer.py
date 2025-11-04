import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9000))
server.listen(1)
print("[서버 대기 중] 포트: 9000")

client, addr = server.accept()
print(f"[클라이언트 연결됨] {addr}")

while True:
    data = client.recv(1024)
    if not data:
        break
    print("받은 메시지:", data.decode())
    client.send(data)  # 받은 그대로 다시 전송

client.close()
server.close()
