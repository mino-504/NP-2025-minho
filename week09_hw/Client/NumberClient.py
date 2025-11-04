import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("서버 IP 입력 (예: 172.18.xxx.xxx): ").strip()
client.connect((server_ip, 9002))
print(f"[서버 연결 성공] {server_ip}:9002")

while True:
    msg = input("두 수 입력 (예: 3,5) [종료:q]: ")
    client.send(msg.encode())

    if msg.lower() == 'q':
        break

    data = client.recv(1024)
    print("서버 응답:", data.decode())

client.close()
print("클라이언트 종료")
