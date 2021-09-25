########################
### YESLAB 网工Python ###
########################

import time
import socket
from multiprocessing import Process
from funSystem.funRouter import CiscoIOSXE

# 此脚本需要完成以下任务：
# 对本机实施2010-2030的端口扫描

def port_scan():
    ip = "127.0.0.1"
    # -------------------作业区域开始------------------------
    # TODO: 修正下面代码中的错误
    client = socket.(socket.AF_INET, socket.SOCK_STREAM)
    for port in range(2010, 2030):
        print("扫描端口：{}".format(port))
        try:
            client.connect(ip, port)
            print("{}的端口{}是开放的".format(ip, port))
            client.send(bytes("Hello", encoding='utf-8'))
            print(client.recv(1024).decode('utf-8'))
            break
        except:
            pass
    client.close()
    # -------------------作业区域结束------------------------


if __name__ == "__main__":
    router = CiscoIOSXE("IOSXE-R1")
    server_proc = Process(target=router.web_manager)
    server_proc.start()
    time.sleep(0.5)
    port_scan()
