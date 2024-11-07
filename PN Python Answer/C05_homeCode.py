########################
### YESLAB 网工Python ###
########################

import time
import socket
import unitTest

ip = "127.0.0.1"
port = 10001
ping_msg = bytes("[Client] 正在 Ping yeslab.server [1.1.1.1] 具有 32 字节的数据", encoding='utf-8')
reply_msg = bytes("[Client] 来自 1.1.1.2 的回复: 字节=32 时间=1ms TTL=1", encoding='utf-8')
# 按照实验手册内容，编写socket的网络PING模拟程序
# -------------------作业区域开始------------------------
# TODO: 建立基本的Server对象
server = socket.socket()
server.bind((ip, port))

# TODO: Server开启监听
server.listen(5)

# TODO: 建立基本的Client对象
client = socket.socket()
client.connect((ip, port))

# TODO: Server开启消息接收等待过程
response, ip = server.accept()

# TODO: Client发送“ping yeslab.server”
client.send(ping_msg)

# TODO: Server接收消息，对ping进行回复
server_recv_msg = response.recv(1024).decode("utf-8")
time.sleep(1)
print(server_recv_msg)
time.sleep(1)
response.send(reply_msg)

# TODO: Client接收消息
client_recv_msg = client.recv(1024).decode("utf-8")
for num in range(4):
    print(client_recv_msg)
    time.sleep(1)
# -------------------作业区域结束------------------------


if __name__ == "__main__":
    unitTest.check_socket_msg_type(server_recv_msg)
    unitTest.check_socket_msg_type(client_recv_msg)
    unitTest.output_error()
    client.close()
    server.close()
