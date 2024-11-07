import socket


class CiscoIOS:
    def __init__(self, HostName):
        self.hostname = HostName
        self.username = "admin"
        self.password = "admin"
        self.device_type = "Cisco IOS"

    def ssh_reply(self):
        print("SSH 2.0 to {} Success".format(self.device_type))


class CiscoIOSXE:
    def __init__(self, HostName):
        self.hostname = HostName
        self.username = "Cadmin"
        self.password = "GuangdongHAHA"
        self.device_type = "Cisco IOS-XE"
        self.intMSG = "GibitEthernet1/0/1 UP 192.168.1.1"

    def ssh_reply(self):
        print("SSH 2.0 to {} Success".format(self.device_type))

    def web_manager(self):
        web_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        web_server.bind(("127.0.0.1", 2021))
        print("交换机的WEB管理已启动！")
        web_server.listen(5)
        msgs = self.reply_msg()
        while True:
            response, ip = web_server.accept()
            recv_msg = response.recv(1024).decode('utf-8')
            if recv_msg == "Hello":
                response.send(msgs[0])
                web_server.close()
                break
            elif recv_msg == "show ip interface brief":
                response.send(msgs[1])
                web_server.close()
                break

    def reply_msg(self):
        msg1 = bytes("[CiscoIOS-XE]欢迎管理员登入！", encoding='utf-8')
        msg2 = bytes("[CiscoIOS-XE] {}".format(self.intMSG), encoding='utf-8')
        return msg1, msg2


class CiscoIOSXR:
    def __init__(self, HostName):
        self.hostname = HostName
        self.username = "ciscoSuper"
        self.password = "Super@super"
        self.device_type = "Cisco IOS-XR"

    def ssh_reply(self):
        print("SSH 2.0 to {} Success".format(self.device_type))


class CiscoNXOS:
    def __init__(self, HostName):
        self.hostname = HostName
        self.username = "NXoperator"
        self.password = "WoShiXinWangGong"
        self.device_type = "Cisco NX-OS"

    def ssh_reply(self):
        print("SSH 2.0 to {} Success".format(self.device_type))