import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("서버 IP 입력 (예: 172.18.xxx.xxx): ").strip()
client.connect((server_ip, 9000))
print(f"[서버 연결 성공] {server_ip}:9000")

while True:
    msg = input("보낼 메시지 (종료:q): ")
    if msg == 'q':
        break
    client.send(msg.encode())
    data = client.recv(1024)
    print("서버 응답:", data.decode())

client.close()
print("클라이언트 종료")
