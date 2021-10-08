import socket

client = socket.socket()
client.connect(("127.0.0.1", 2001))
while True:
    hello = client.recv(1024).decode("utf-8")
    if hello:
        print(hello)
        cmd = input("【client】请输入命令:")
        client.send(bytes(cmd, encoding="utf-8"))
        if cmd == "exit":
            break
client.close()