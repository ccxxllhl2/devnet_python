import random


class SYSTEM:
    def __init__(self, sys_name):
        print("欢迎登录【{}】系统！".format(sys_name))
        self.database = {}
        while True:
            action = input("【0】用户注册\n【1】用户登录\n请选择:")
            if action == "0":
                username = input("请输入您想要注册的用户名: ")
                password = input("请输入您想要注册的密码: ")
                self.sign_up(username, password)
                continue
            elif action == "1":
                self.sign_in()
                break
            else:
                print("请您按提示输入！")
                continue

    def sign_up(self, username, password):
        self.database[username] = password
        print("{}用户注册成功！".format(username))

    def sign_in(self):
        while True:
            username = input("请输入您想要登录的用户名: ")
            password = input("请输入您想要登录的密码: ")
            if username not in self.database.keys():
                print("该用户未注册，请重新登录！")
                continue
            elif password != self.database[username]:
                print("密码错误请重新登录！")
                continue
            else:
                print("登录成功，欢迎您：{}".format(username))
                break


class NET_OPS(SYSTEM):
    def __init__(self):
        super().__init__("Network System")
        self.cpu_limit = 60
        self.mem_limit = 50
        self.delay = 300
        for i in range(5):
            print("-"*10)
            self.cpu_monitor()
            self.mem_monitor()
            self.delay_monitor()

    def cpu_monitor(self):
        cpu_usage = random.randint(0, 100)
        if cpu_usage > self.cpu_limit:
            print("【Warning】CPU负载过高:{}".format(cpu_usage))

    def mem_monitor(self):
        mem_usage = random.randint(0, 100)
        if mem_usage > self.mem_limit:
            print("【Warning】内存负载过高:{}".format(mem_usage))

    def delay_monitor(self):
        net_delay = random.randint(0, 1000)
        if net_delay > self.delay:
            print("【Warning】网络延迟过高:{}".format(net_delay))


if __name__ == "__main__":
    my_system = NET_OPS()
