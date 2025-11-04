import socket
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9001))  # 모든 IP 접근 허용
server.listen(1)
print("[서버 대기 중] 포트: 9001")

client, addr = server.accept()
print(f"[클라이언트 연결됨] {addr}")

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
client.send(current_time.encode())

client.close()
server.close()
