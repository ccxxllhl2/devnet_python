import socket

server = socket.socket()
server.bind(("127.0.0.1", 2001))
server.listen(5)
reply, address = server.accept()
reply.send(bytes("【Server】来自 {} 的朋友你好！".format(address), encoding="utf-8"))
while True:
    cmd = reply.recv(1024).decode("utf-8")
    if cmd == "exit":
        break
    elif cmd != "exit":
        reply.send(bytes("【Server】请输入正确命令！".format(address), encoding="utf-8"))
reply.close()