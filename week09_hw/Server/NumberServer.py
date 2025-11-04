import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9002))
server.listen(1)
print("[서버 대기 중] 포트: 9002")

client, addr = server.accept()
print(f"[클라이언트 연결됨] {addr}")

while True:
    data = client.recv(1024)
    if not data:
        break

    msg = data.decode().strip()
    if msg.lower() == 'q':
        break

    try:
        a, b = map(int, msg.split(','))
        result = a + b
        response = f"결과: {result}"
    except:
        response = "형식 오류 (예: 3,5)"

    client.send(response.encode())

client.close()
server.close()
