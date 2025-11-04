import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input("서버 IP 입력 (예: 172.18.xxx.xxx): ").strip()
client.connect((server_ip, 9001))

data = client.recv(1024).decode()
print("서버 시각:", data)

client.close()
